from BayesNet.loadBayesNet import loadInBayesNet

def main():
    
    BN = loadInBayesNet('./datasetUniform/dag25.json')

    query = 10
    evidence = {
        1: 1,
        2: 1,
        3: 0,
        4: 0,
        6: 1,
        7: 1,
        8: 0,
        9: 0
    }
    # evidence = {}
    numSamples = 1000

    W = BN.likelihoodWeighting_Query(query, evidence, numSamples)
    print(W)

    (G, sampleG) = BN.gibbsAsk_Query(query, evidence, numSamples)
    print(G)

    MH = BN.metropolisHasting_Query(query, evidence, numSamples, 0.75)
    print(MH)
    
if __name__ == "__main__":
    main()