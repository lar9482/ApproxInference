class testParam:
    def __init__(self, testName, filePath, query, evidenceBegin, evidenceEnd):
        self.testName = testName
        self.filePath = filePath
        self.query = query
        self.evidenceBegin = evidenceBegin
        self.evidenceEnd = evidenceEnd

"""
    For each of these graphs test cases.
    query the middle variable, and set the evidence to the beginning and ending variables
    according to the topological order of the networks
"""

def getDAGParams():
    dagParams = [
        testParam(
            'datasetUniform_dag10.xlsx',
            './dataset/datasetUniform/dag10.json',
            7,
            {6: 0, 8: 0, 9: 0},
            {3: 0, 0: 0, 2: 0}
        ),
        testParam(
            'datasetUniform_dag20.xlsx',
            './dataset/datasetUniform/dag20.json',
            10,
            {18: 0, 19: 0, 17: 0, 14: 0, 16: 0},
            {7: 0, 1: 0, 3: 0, 5: 0, 2: 0}
        )
    ]

    return dagParams

def getUniformParams():
    uniformParams = [
    testParam(
        'datasetUniform_polytree5.xlsx',
        './dataset/datasetUniform/polytree5.json',
        3,
        { 0: 0, 1: 0 },
        { 2: 0, 4: 0 }
    ),
    testParam(
        'datasetUniform_polytree15.xlsx',
        './dataset/datasetUniform/polytree15.json',
        7,
        {0: 0, 1: 0, 2: 0, 4: 0},
        {10: 0, 14: 0, 13: 0, 12: 0},
    ),
    testParam(
        'datasetUniform_polytree25.xlsx',
        './dataset/datasetUniform/polytree25.json',
        20,
        {0: 0, 1: 0, 2: 0, 3: 0, 6: 0, 7: 0},
        {13: 0, 17: 0, 18: 0, 22: 0, 24: 0, 19: 0}
    )]

    return uniformParams

def getNearZeroParams():
    nearZeroParams = [
    testParam(
        'datasetNearZero_polytree5.xlsx',
        './dataset/datasetNearZero/polytree5.json',
        2,
        {0: 0, 1: 0},
        {3: 0, 4: 0}
    ),
    testParam(
        'datasetNearZero_polytree15.xlsx',
        './dataset/datasetNearZero/polytree15.json',
        6,
        {0: 0, 1: 0, 2: 0, 3: 0},
        {14: 0, 12: 0, 13: 0, 11: 0}
    ),
    testParam(
        'datasetNearZero_polytree25.xlsx',
        './dataset/datasetNearZero/polytree25.json',
        11,
        {0: 0, 1: 0, 6: 0, 8: 0, 14: 0, 2: 0},
        {21: 0, 5: 0, 20: 0, 22: 0, 23: 0, 7: 0}
    )]

    return nearZeroParams

def getNearOneParams():
    nearOneParams = [
    testParam(
        'datasetNearOne_polytree5.xlsx',
        './dataset/datasetNearOne/polytree5.json',
        2,
        {0: 0, 1: 0},
        {3: 0, 4: 0}
    ),
    testParam(
        'datasetNearOne_polytree15.xlsx',
        './dataset/datasetNearOne/polytree15.json',
        12,
        {0: 0, 1: 0, 2: 0, 5: 0},
        {14: 0, 11: 0, 9: 0, 13: 0}
    ),
    testParam(
        'datasetNearOne_polytree25.xlsx',
        './dataset/datasetNearOne/polytree25.json',
        10,
        {0: 0, 1: 0, 4: 0, 12: 0, 2: 0, 3: 0},
        {16: 0, 18: 0, 20: 0, 13: 0, 21: 0, 24: 0}
    )]

    return nearOneParams