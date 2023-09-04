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
        self.children = [] # Children will be determined, once all of the nodes are loaded into the bayes net
    
    """
        @param nodeValue: Integer
            The actual value that the current RV is assigned. This required for determining the probability
            in a bernoulli random variable.

        @param parentValues: List(Integer)/Tuple(Integer)
            The actual valules that the parent RVs are assigned. These are necessary to actually
            query the CPT for the probability itself
    """
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