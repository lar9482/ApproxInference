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