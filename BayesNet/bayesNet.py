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

class BayesNet:
    """
        @param allNodes: {integer: BayesNode}
            Dictionary of BayesNodes where the key is the node id
    """
    def __init__(self, allNodes):
        self.allNodes = allNodes
    
    def getTopologicalOrder(self):
        sortedNodes = []
        inDegrees = {}

        for nodeId in list(self.allNodes.keys()):
            inDegrees[nodeId] = 0

        # Initialize the edges to the parents
        for nodeId in list(self.allNodes.keys()):
            for parentId in self.allNodes[nodeId].parents:
                inDegrees[parentId] += 1
        
        #Finding the nodes that don't have parents
        queue = []
        for nodeId in list(self.allNodes.keys()):
            if inDegrees[nodeId] == 0:
                queue.append(nodeId)
        
        while (len(queue) > 0):
            currNodeId = queue.pop(0)

            sortedNodes.append(currNodeId)
            for parentId in self.allNodes[currNodeId].parents:
                inDegrees[parentId] -= 1

                if (inDegrees[parentId] == 0):
                    queue.append(parentId)
        
        # The topological algorithm was performed backwards, so a reversal is required.
        return list(reversed(sortedNodes))