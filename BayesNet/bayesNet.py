import random
import copy

class BayesNet:
    """
        @param allNodes: {integer: BayesNode}
            Dictionary of BayesNodes where the key is the node id
    """
    def __init__(self, allNodes):
        self.allNodes = allNodes
        self.__determineChildren()
        
    def __determineChildren(self):
        for nodeId in list(self.allNodes.keys()):
            for otherNodeId in list(self.allNodes.keys()):
                if (otherNodeId == nodeId):
                    continue
                elif (nodeId in self.allNodes[otherNodeId].parents):
                    self.allNodes[nodeId].children.append(otherNodeId)
    
    def __getTopologicalOrder(self):

        # Initialize dict that keeps track of incoming edges.
        inDegree = {}
        for nodeId in list(self.allNodes.keys()):
            inDegree[nodeId] = 0

        # Counting the number of incoming edges for the child nodes
        for nodeId in list(self.allNodes.keys()):
            for childNodeId in self.allNodes[nodeId].children:
                inDegree[childNodeId] += 1

        queue = list(nodeId for nodeId in list(self.allNodes.keys()) if inDegree[nodeId] == 0)
        order = []

        while (len(queue) > 0):
            nodeId = queue.pop(0)
            order.append(nodeId)

            # Reduce the number of tracked edge counts for the child nodes
            for childId in self.allNodes[nodeId].children:
                inDegree[childId] -= 1

                if inDegree[childId] == 0:
                    queue.append(childId)
        
        return order

    # Initializing the sample with values that are fixed by the evidence. 
    def __getInitialSample_FixedByEvidence(self, evidence):
        sample = {}
        for nodeId in list(self.allNodes.keys()):
            if (evidence.get(nodeId) != None):
                sample[nodeId] = evidence[nodeId]
            else:
                sample[nodeId] = 0
        
        return sample
    
    def __normalizeVector(self, vector):
        sumOfWeightedCounts = sum(list(vector.values()))

        for value in list(vector.keys()):
            if (sumOfWeightedCounts > 0):
                vector[value] /= sumOfWeightedCounts
        
        return vector
    
    ####################################################################################################
    # Likelihood weighting specific methods. It basically implements weighted sampling in the network. #
    ####################################################################################################
    def __sampleValueFromNetwork(self, queryId, evidence):
        prob = self.allNodes[queryId].cpt[evidence]
        chance = random.uniform(0, 1)

        if (chance < prob):
            return 1
        else:
            return 0
    
    def __getWeightedSample(self, evidence):
        weight = 1
        event = self.__getInitialSample_FixedByEvidence(evidence)

        for nodeId in self.__getTopologicalOrder():
            nodeVariable = self.allNodes[nodeId]
            parentIds = nodeVariable.parents

            #Update the weight using parentValues from event if 'nodeId' is an evidence variable
            if nodeId in list(evidence.keys()):
                nodeValueFromEvent = event[nodeId]
                parentValuesFromEvent = [event[parentId] for parentId in parentIds]
                prob = nodeVariable.lookUpProb_givenNodeAndParentValues(nodeValueFromEvent, parentValuesFromEvent)
                
                weight *= prob
            
            #Else, sample from the nodeID given parent values from the event.
            else:
                localEvidenceFromEvent = [event[parentId] for parentId in parentIds]
                sampledValue = self.__sampleValueFromNetwork(nodeId, tuple(localEvidenceFromEvent))

                event[nodeId] = sampledValue
        
        return (event, weight)
    
    ##########################################################################################################
    # Gibbs specific methods. Basically, they deal with sampling and prob. distribution on a markov blanket. #
    ##########################################################################################################
    def __sampleFromMarkovBlanket(self, query, currNetworkState):
        probDistribution = {0: 0, 1: 0}

        positiveNetworkState = copy.deepcopy(currNetworkState)
        negativeNetworkState = copy.deepcopy(currNetworkState)
        positiveNetworkState[query] = 1
        negativeNetworkState[query] = 0

        probDistribution[0] = self.__calcMarkovBlanketProb_givenQueryAndSample(query, negativeNetworkState)
        probDistribution[1] = self.__calcMarkovBlanketProb_givenQueryAndSample(query, positiveNetworkState)

        probDistribution = self.__normalizeVector(probDistribution)

        chance = random.uniform(0, 1)
        if (chance < probDistribution[1]):
            return 1
        else:
            return 0
        
    def __calcMarkovBlanketProb_givenQueryAndSample(self, query, networkStateSample):
        prob = 1

        parentValues = [networkStateSample[parentId] for parentId in self.allNodes[query].parents]
        queryValue = networkStateSample[query]
        prob *= self.allNodes[query].lookUpProb_givenNodeAndParentValues(
            queryValue, 
            tuple(parentValues)
        )

        for childId in self.allNodes[query].children:
            parentOfChildValues = [networkStateSample[parentId] for parentId in self.allNodes[childId].parents]
            childValue = networkStateSample[childId]
            prob *= self.allNodes[childId].lookUpProb_givenNodeAndParentValues(
                childValue, 
                tuple(parentOfChildValues)
            )
        
        return prob
    
    def __calcSampleWeight_BasedOnEvidence(self, sample, evidence):
        weight = 1

        for nodeId in self.__getTopologicalOrder():
            nodeVariable = self.allNodes[nodeId]
            parentIds = nodeVariable.parents

            #Update the weight using parentValues from event if 'nodeId' is an evidence variable
            if nodeId in list(evidence.keys()):
                nodeValueFromSample = sample[nodeId]
                parentValuesFromSample = [sample[parentId] for parentId in parentIds]
                prob = nodeVariable.lookUpProb_givenNodeAndParentValues(nodeValueFromSample, parentValuesFromSample)
                
                weight *= prob
        
        return weight
    """
        @param query: Integer
            The node id to be queried from the network

        @param evidence: {Integer: Integer} (NodeID: NodeValue)
            This dictionary will map the evidence node is to its given node value

        @param N: Integer
            The number of samples to calculate
    """
    def likelihoodWeighting_Query(self, query, evidence, N):
        W = {0: 0, 1: 0}

        for _ in range(0, N):
            (event, weight) = self.__getWeightedSample(evidence)
            queryValue = event[query]
            W[queryValue] += weight
        
        return self.__normalizeVector(W)

    """
        @param query: Integer
            The node id to be queried from the network

        @param evidence: {Integer: Integer} (NodeID: NodeValue)
            This dictionary will map the evidence node is to its given node value

        @param N: Integer
            The number of samples to calculate
    """
    def gibbsAsk_Query(self, query, evidence, N):

        C = {0: 0, 1: 0}
        nonEvidenceNodeIds = [nonEvidenceId 
             for nonEvidenceId in list(self.allNodes.keys()) 
             if not (nonEvidenceId in list(evidence.keys()))]
        
        currNetworkState = self.__getInitialSample_FixedByEvidence(evidence)
        
        for _ in range(0, N):
            nonEvidenceId = random.choice(nonEvidenceNodeIds)
            sampledValue = self.__sampleFromMarkovBlanket(nonEvidenceId, currNetworkState)
            currNetworkState[nonEvidenceId] = sampledValue

            C[currNetworkState[query]] += 1
        
        return (self.__normalizeVector(C), currNetworkState)
    
    def metropolisHasting_Query(self, query, evidence, N, P):
        distribution = {0: 0, 1: 0}
        sample = self.__getInitialSample_FixedByEvidence(evidence)

        while (N >= 0):
            chance = random.uniform(0, 1)

            if (chance < P):
                (gibbsProbDis, gibbsSample) = self.gibbsAsk_Query(query, evidence, 50)
                sample = gibbsSample
            else:
                (newSample, weight) = self.__getWeightedSample(sample)
                sample = newSample

            distribution[sample[query]] += 1
            N -= 1
        
        return self.__normalizeVector(distribution)