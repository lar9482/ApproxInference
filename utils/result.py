class testResult:
    def __init__(self, 
            testName,
            numSamples,
            numTrials,
            PFalse,
            PTrue,
            runTime
    ):
        self.testName = testName
        self.numSamples = numSamples
        self.numTrials = numTrials
        self.PFalse = PFalse
        self.PTrue = PTrue
        self.runTime = runTime

class exactResult:
    def __init__(self,
                 testName, 
                 PFalse, 
                 PTrue, 
                 runTime):
        self.testName = testName
        self.PFalse = PFalse
        self.PTrue = PTrue
        self.runTime = runTime