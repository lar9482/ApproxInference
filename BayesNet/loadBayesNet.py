from BayesNet.bayesNet import BayesNet
from BayesNet.bayesNode import BayesNode

import json
"""
    @param filename: string
        The file name of the json file to load in the bayes net.
    
    @Returns BayesNet:
        The actual bayes net representation of the inputted file.
"""
def loadInBayesNet(filename):
    rawBayesNetData = json.load(open(filename))
    allBayesNodes = {}

    for nodeId in rawBayesNetData:
        parentIds = rawBayesNetData[nodeId]['parents']
        cptTable = {}
        for cptEntry in rawBayesNetData[nodeId]['prob']:
            parentValues = cptEntry[0]
            probability = cptEntry[1]
            cptTable[tuple(parentValues)] = probability
        
        newBayesNode = BayesNode(
            int(nodeId),
            parentIds,
            cptTable
        )
        allBayesNodes[int(nodeId)] = newBayesNode
    
    return BayesNet(allBayesNodes)