from testing.testingSuite import runTestingSuite
from utils.datasetParams import getUniformParams, getNearZeroParams, getNearOneParams
from utils.exact_inference import Bayes_Net
from utils.result import exactResult
import time
import openpyxl

def getExactResults(testName, fileLoc, query, evidence):
    bn = Bayes_Net()
    bn.create_from_json(fileLoc)
    starttime = time.time()
    exact_enum = dict(bn.enumeration_ask(query, evidence))
    endtime = time.time()
    exact_time = (endtime-starttime)

    return exactResult(
        testName,
        exact_enum[0],
        exact_enum[1],
        exact_time
    )


def runExactSuite(datasetParams):
    workbook = openpyxl.load_workbook('./results/exactResults.xlsx')
    sheet = workbook.active

    for datasetParam in datasetParams:
        beginExactResult = getExactResults(
            datasetParam.testName, 
            datasetParam.filePath, 
            datasetParam.query, 
            datasetParam.evidenceBegin
        )

        endExactResult = getExactResults(
            datasetParam.testName, 
            datasetParam.filePath, 
            datasetParam.query, 
            datasetParam.evidenceEnd
        )

        sheet.append([beginExactResult.testName + 'beginOrder', beginExactResult.PFalse, beginExactResult.PTrue, beginExactResult.runTime])
        sheet.append([endExactResult.testName + 'endOrder', endExactResult.PFalse, endExactResult.PTrue, endExactResult.runTime])

    workbook.save('./results/exactResults.xlsx')
    workbook.close()

def main():
    # runExactSuite(getUniformParams())
    # runExactSuite(getNearZeroParams())
    # runExactSuite(getNearOneParams())
    pass