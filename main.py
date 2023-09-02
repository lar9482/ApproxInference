from BayesNet.loadBayesNet import loadInBayesNet

def main():
    
    BN = loadInBayesNet('./Reference/polytree50.json')

    query = 5
    evidence = {
        0: 0,
        4: 1,
        10: 1,
        25: 0,
        45: 1
    }
    numSamples = 500

    W = BN.likelihoodWeighting_Query(query, evidence, numSamples)
    
if __name__ == "__main__":
    main()