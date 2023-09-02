import random

class BayesNode:
    """
        @param nodeId: Integer
            The id(name) for this particular node

        @param parentIds: List(Integer)
            Just a list of integers that point to the parent node ids
        
        @param cpt: {(v1, v2,...,vn): float}
            A dictionary to represent the conditional probability table in this node.

            - The key represents a tuple of values sampled from all of the parent nodes.

            - The value represents the probability of the node's value being 1 based on the values of the parents.
              P(<node_id>=1|<parents>=<assignment>)=<probability>
    """
    def __init__(self, nodeId, parentIds, cpt):
        self.nodeId = nodeId
        self.parents = parentIds
        self.cpt = cpt
        self.children = []
    
    def lookUpProb_givenNodeAndParentValues(self, nodeValue, parentValues):
        if isinstance(parentValues, list):
            prob = self.cpt[tuple(parentValues)]

            if (nodeValue == 0):
                return (1 - prob)
            elif (nodeValue == 1):
                return prob      
            else:
                raise ValueError('nodeValue is not a bernoulli variable')
        elif isinstance(parentValues, tuple):
            prob = self.cpt[parentValues]

            if (nodeValue == 0):
                return (1 - prob)
            elif (nodeValue == 1):
                return prob
            else:
                raise ValueError('nodeValue is not a bernoulli variable')
        else:
            raise ValueError('parentValues is neither a list nor tuple')

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

            # Reduce the number of tracked edge counts
            for childId in self.allNodes[nodeId].children:
                inDegree[childId] -= 1

                if inDegree[childId] == 0:
                    queue.append(childId)
        
        return order

    def __sampleValueFromNetwork(self, queryId, evidence):
        prob = self.allNodes[queryId].cpt[evidence]
        chance = random.uniform(0, 1)

        if (chance < prob):
            return 1
        else:
            return 0
    
    def __getWeightedSample(self, evidence):
        weight = 1
        event = {}

        # Initializing the vector with evidences that are fixed by the evidence. 
        for nodeId in list(self.allNodes.keys()):
            if (evidence.get(nodeId) != None):
                event[nodeId] = evidence[nodeId]
            else:
                event[nodeId] = 0

        for nodeId in self.__getTopologicalOrder():
            parentIds = self.allNodes[nodeId].parents

            if nodeId in list(evidence.keys()):
                nodeValue = event[nodeId]
                parentValues = [event[parentId] for parentId in parentIds]
                prob = self.allNodes[nodeId].lookUpProb_givenNodeAndParentValues(nodeValue, parentValues)
                
                weight *= prob
            else:
                localEvidence = [event[parentId] for parentId in parentIds]
                sampledValue = self.__sampleValueFromNetwork(nodeId, tuple(localEvidence))

                event[nodeId] = sampledValue
        
        return (event, weight)

    def __normalizeVector(self, vector):
        sumOfWeightedCounts = sum(list(vector.values()))

        for value in list(vector.keys()):
            vector[value] /= sumOfWeightedCounts
        
        return vector
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