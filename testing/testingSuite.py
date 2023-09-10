from BayesNet.loadBayesNet import loadInBayesNet
from utils.result import testResult

from openpyxl import Workbook
from multiprocessing import Manager, Lock, Process

import time


def runLikelihoodWeighting_Test(name, BN, query, evidence, numSamples, numTrials):
    startTime = time.time()
    W = BN.likelihoodWeighting_Query(query, evidence, numSamples)
    endTime = time.time()

    return testResult(
        name,
        numSamples,
        numTrials,
        W[0],
        W[1],
        endTime - startTime
    )

def runGibbsAsk_Test(name, BN, query, evidence, numSamples, numTrials):
    startTime = time.time()
    (C, sample) = BN.gibbsAsk_Query(query, evidence, numSamples)
    endTime = time.time()

    return testResult(
        name,
        numSamples,
        numTrials,
        C[0],
        C[1],
        endTime - startTime
    )

def runMetropolisHasting_Test(
        name, 
        BN, 
        query, 
        evidence, 
        P, 
        numSamples, 
        numTrials,
        sharedTestResults,
        lock
    ):
    startTime = time.process_time()
    MH = BN.metropolisHasting_Query(query, evidence, numSamples, P)
    endTime = time.process_time()

    newTestResult = testResult(
        name,
        numSamples,
        numTrials,
        MH[0],
        MH[1],
        endTime - startTime
    )

    lock.acquire()
    sharedTestResults.append(newTestResult)
    lock.release()

def runParallelMetropolisHasting_Tests(name, BN, query, evidence, P, numSamples, numTrials):
    mhResults = []

    with Manager() as manager:
        allProcesses = []
        lock = manager.Lock()
        sharedTestResults = manager.list()

        for _ in range(0, numTrials):
            metroHastProcess = Process(
                target=runMetropolisHasting_Test,
                args=(
                    name, BN, query, evidence, P, numSamples, numTrials,
                    sharedTestResults,
                    lock
                )
            )
            allProcesses.append(metroHastProcess)
        
        for process in allProcesses:
            process.start()
        
        for process in allProcesses:
            process.join()
        
        mhResults = list(sharedTestResults)
    
    return mhResults

def runTestingSuite(datasetParams, excelName, numSamples = 1000, numTrials = 10):
    for param in datasetParams:

        BN = loadInBayesNet(param.filePath)
        testResults = []

        for _ in range(0, numTrials):
            testLWBegin_Result = runLikelihoodWeighting_Test(
                'Likelihood_BeginOrder',                                        
                BN, 
                param.query, 
                param.evidenceBegin, 
                numSamples, 
                numTrials
            )
            testResults.append(testLWBegin_Result)
        
        for _ in range(0, numTrials):
            testLWEnd_Result = runLikelihoodWeighting_Test(
                'Likelihood_EndOrder',                                        
                BN, 
                param.query, 
                param.evidenceEnd, 
                numSamples, 
                numTrials
            )
            testResults.append(testLWEnd_Result)

        print('Finished likelihood weighting suite')

        ######################################################################################

        for _ in range(0, numTrials):
            testGABegin_Result = runGibbsAsk_Test(
                'Gibbs_BeginOrder',
                BN, 
                param.query, 
                param.evidenceBegin, 
                numSamples, 
                numTrials
            )
            testResults.append(testGABegin_Result)
        
        for _ in range(0, numTrials):
            testGAEnd_Result = runGibbsAsk_Test(
                'Gibbs_EndOrder',
                BN, 
                param.query, 
                param.evidenceEnd, 
                numSamples, 
                numTrials
            )
            testResults.append(testGAEnd_Result)

        print('Finished gibbs ask suite')

        ######################################################################################
        
        testMHBegin_Result = runParallelMetropolisHasting_Tests(
            'MetroHast_BeginOrder0.75',
            BN, 
            param.query, 
            param.evidenceBegin, 
            0.75,
            numSamples, 
            numTrials
        )
        testResults.extend(testMHBegin_Result)

        print('Finished beginning portion of Metropolis Hasting for 0.75')
        
        testMHEnd_Result = runParallelMetropolisHasting_Tests(
            'MetroHast_EndOrder0.75',
            BN, 
            param.query, 
            param.evidenceEnd, 
            0.75,
            numSamples, 
            numTrials
        )
        testResults.extend(testMHEnd_Result)

        print('Finished final portion of Metropolis Hasting for 0.75')
        print('Finished metropolis 0.75 suite')

        ######################################################################################
        
        testMHBegin_Result = runParallelMetropolisHasting_Tests(
            'MetroHast_BeginOrder0.85',
            BN, 
            param.query, 
            param.evidenceBegin, 
            0.85,
            numSamples, 
            numTrials
        )
        testResults.extend(testMHBegin_Result)

        print('Finished beginning portion of Metropolis Hasting for 0.85')
        
        testMHEnd_Result = runParallelMetropolisHasting_Tests(
            'MetroHast_EndOrder0.85',
            BN, 
            param.query, 
            param.evidenceEnd, 
            0.85,
            numSamples, 
            numTrials
        )
        testResults.extend(testMHEnd_Result)

        print('Finished final portion of Metropolis Hasting for 0.85')
        print('Finished metropolis 0.85 suite')

        ######################################################################################
        
        testMHBegin_Result = runParallelMetropolisHasting_Tests(
            'MetroHast_BeginOrder0.95',
            BN, 
            param.query, 
            param.evidenceBegin, 
            0.95,
            numSamples, 
            numTrials
        )
        testResults.extend(testMHBegin_Result)

        print('Finished beginning portion of Metropolis Hasting for 0.95')

        testMHEnd_Result = runParallelMetropolisHasting_Tests(
            'MetroHast_EndOrder0.95',
            BN, 
            param.query, 
            param.evidenceEnd, 
            0.95,
            numSamples, 
            numTrials
        )
        testResults.extend(testMHEnd_Result)

        print('Finished final portion of Metropolis Hasting for 0.95')
        print('Finished metropolis 0.95 suite')

        # Create a new Excel workbook
        workbook = Workbook()
        sheet = workbook.active

        # Add headers
        sheet.append(['TestName', 'NumSamples', 'NumTrials', 'PFalse', 'PTrue', 'RunTime(sec)'])

        for testResult in testResults:
            sheet.append([
                testResult.testName,
                testResult.numSamples,
                testResult.numTrials,
                testResult.PFalse,
                testResult.PTrue,
                testResult.runTime
            ])
        
        workbook.save(excelName + param.testName)