class testParam:
    def __init__(self, filePath, query, evidenceBegin, evidenceEnd):
        self.filePath = filePath
        self.query = query
        self.evidenceBegin = evidenceBegin
        self.evidenceEnd = evidenceEnd

"""
    For each of these graphs.
    query the middle variable, and set the evidence to the beginning and ending variables
    according to the topological order of the networks
"""
def getUniformParams():
    uniformParams = [
    testParam(
        './dataset/datasetUniform/polytree5.json',
        3,
        { 0: 0, 1: 0 },
        { 2: 0, 4: 0 }
    ),
    testParam(
        './dataset/datasetUniform/polytree15.json',
        7,
        {0: 0, 1: 0, 2: 0, 4: 0},
        {10: 0, 14: 0, 13: 0, 12: 0},
    ),
    testParam(
        './dataset/datasetUniform/polytree25.json',
        20,
        {0: 0, 1: 0, 2: 0, 3: 0, 6: 0, 7: 0},
        {13: 0, 17: 0, 18: 0, 22: 0, 24: 0, 19: 0}
    ),
    testParam(
        './dataset/datasetUniform/dag5.json',
        2,
        { 3: 0, 4: 0 },
        { 1: 0, 0: 0 }
    ),
    testParam(
        './dataset/datasetUniform/dag15.json',
        8,
        {13: 0, 14: 0, 11: 0, 12: 0},
        {4: 0, 0: 0, 3: 0, 1: 0}
    ),
    testParam(
        './dataset/datasetUniform/dag25.json',
        9,
        {22: 0, 24: 0, 23: 0, 18: 0, 20: 0, 21: 0},
        {12: 0, 9: 0, 1: 0, 4: 0, 5: 0, 7: 0}
    )]

    return uniformParams

def getNearZeroParams():
    nearZeroParams = [
    testParam(
        './dataset/datasetNearZero/polytree5.json',
        2,
        {0: 0, 1: 0},
        {3: 0, 4: 0}
    ),
    testParam(
        './dataset/datasetNearZero/polytree15.json',
        6,
        {0: 0, 1: 0, 7: 0, 2: 0},
        {4: 0, 8: 0, 14: 0, 13: 0}
    ),
    testParam(
        './dataset/datasetNearZero/polytree25.json',
        8,
        {0: 0, 1: 0, 4: 0, 5: 0, 23: 0, 2: 0},
        {20: 0, 24: 0, 15: 0, 22: 0, 13: 0, 17: 0}
    ),
    testParam(
        './dataset/datasetNearZero/dag5.json',
        4,
        {2: 0, 3: 0},
        {0: 0, 1: 0}
    ),
    testParam(
        './dataset/datasetNearZero/dag15.json',
        6,
        {14: 0, 9: 0, 13: 0, 11: 0},
        {2: 0, 1: 0, 5: 0, 0: 0}
    ),
    testParam(
        './dataset/datasetNearZero/dag25.json',
        9,
        {23: 0, 24: 0, 22: 0, 21: 0, 20: 0, 18: 0},
        {3: 0, 10: 0, 1: 0, 6: 0, 8: 0, 0: 0}
    )]

    return nearZeroParams

def getNearOneParams():
    nearOneParams = [
    testParam(
        './dataset/datasetNearOne/polytree5.json',
        2,
        {0: 0, 1: 0},
        {3: 0, 4: 0}
    ),
    testParam(
        './dataset/datasetNearOne/polytree15.json',
        13,
        {0: 0, 1: 0, 2: 0, 4: 0},
        {11: 0, 9: 0, 12: 0, 14: 0}
    ),
    testParam(
        './dataset/datasetNearOne/polytree25.json',
        22,
        {0: 0, 1: 0, 2: 0, 11: 0, 13: 0, 3: 0},
        {16: 0, 24: 0, 15: 0, 17: 0, 12: 0, 19: 0}
    ),
    testParam(
        './dataset/datasetNearOne/dag5.json',
        3,
        {4: 0, 1: 0},
        {2: 0, 0: 0}
    ),
    testParam(
        './dataset/datasetNearOne/dag15.json',
        10,
        {12: 0, 13: 0, 14: 0, 9: 0},
        {0: 0, 4: 0, 2: 0, 1: 0}
    ),
    testParam(
        './dataset/datasetNearOne/polytree25.json',
        14,
        {22: 0, 23: 0, 24: 0, 21: 0, 20: 0, 15: 0},
        {6: 0, 9: 0, 3: 0, 1: 0, 0: 0, 4: 0}
    )]

    return nearOneParams