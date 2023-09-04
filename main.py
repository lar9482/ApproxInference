from BayesNet.loadBayesNet import loadInBayesNet

def main():
    
    BN = loadInBayesNet('./Reference/polytree10.json')

    query = 3
    evidence = {}
    # evidence = {}
    numSamples = 1000

    W = BN.likelihoodWeighting_Query(query, evidence, numSamples)
    print(W)

    (G, sampleG) = BN.gibbsAsk_Query(query, evidence, numSamples)
    print(G)

    MH = BN.metropolisHasting_Query(query, evidence, numSamples, 0.90)
    print(MH)
    
if __name__ == "__main__":
    main()