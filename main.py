from testing.testingSuite import runTestingSuite
from utils.datasetParams import getUniformParams, getNearZeroParams, getNearOneParams, getDAGParams
from utils.exact_inference import Bayes_Net
from BayesNet.bayesNet import BayesNet
from utils.result import exactResult
from BayesNet.loadBayesNet import loadInBayesNet
from testing.exactInferenceSuite import runExactSuite
import time
import openpyxl

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def printFileContent(filename, allTestNames):
    fileDF = pd.read_excel('./results/' + filename, engine='openpyxl')

    for testName in allTestNames:

        queryMask = (fileDF['TestName'] == testName)
        subDF = fileDF[queryMask]

        print(testName)

        print('PTrue')
        print('Mean: ' + str("{:.5f}".format(subDF['PTrue'].mean())))
        print('STD: ' + str("{:.5f}".format(subDF['PTrue'].std())))
        print()
        print('PFalse')
        print('Mean: ' + str("{:.5f}".format(subDF['PFalse'].mean())))
        print('STD: ' + str("{:.5f}".format(subDF['PFalse'].std())))
        print()
        print('RunTime(sec)')
        print('Mean: ' + str("{:.5f}".format(subDF['RunTime(sec)'].mean())))
        print('STD: ' + str("{:.5f}".format(subDF['RunTime(sec)'].std())))
        print()
        print('#####################################################################')

def main():
    numSamples = 5000
    numTrials = 25
    excelBasePath = './results/'
    runExactSuite(getDAGParams())
    runTestingSuite(getUniformParams(), excelBasePath, numSamples, numTrials)
    runTestingSuite(getNearZeroParams(), excelBasePath, numSamples, numTrials)
    runTestingSuite(getNearOneParams(), excelBasePath, numSamples, numTrials)
    runTestingSuite(getDAGParams(), excelBasePath, numSamples, numTrials)

    testNames = [
        'Likelihood_BeginOrder',
        'Likelihood_EndOrder',
        'Gibbs_BeginOrder',
        'Gibbs_EndOrder',
        'MetroHast_BeginOrder0.75',
        'MetroHast_EndOrder0.75',
        'MetroHast_BeginOrder0.85',
        'MetroHast_EndOrder0.85',
        'MetroHast_BeginOrder0.95',
        'MetroHast_EndOrder0.95'
    ]

    printFileContent('datasetNearOne_polytree25.xlsx', testNames)

if __name__ == "__main__":
    main()