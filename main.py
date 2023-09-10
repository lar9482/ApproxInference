from testing.testingSuite import runTestingSuite
from utils.datasetParams import getUniformParams, getNearZeroParams, getNearOneParams
from utils.exact_inference import Bayes_Net
from utils.result import exactResult
import time
import openpyxl

def main():
    numSamples = 1000
    numTrials = 25
    excelBasePath = './results/'
    runTestingSuite(getUniformParams(), excelBasePath, numSamples, numTrials)
    runTestingSuite(getNearZeroParams(), excelBasePath, numSamples, numTrials)
    runTestingSuite(getNearOneParams(), excelBasePath, numSamples, numTrials)

if __name__ == "__main__":
    main()