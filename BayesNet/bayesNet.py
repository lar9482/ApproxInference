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
        @param allNodes: List(BayesNode)
            Simply a list of 'BayesNode' that represent all of the nodes in the bayesian network.
    """
    def __init__(self, allNodes):
        self.allNodes = allNodes