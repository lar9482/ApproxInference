from BayesNet.loadBayesNet import loadInBayesNet

def main():
    
    BN = loadInBayesNet('./dataset/datasetNearOne/dag25.json')

    query = 9
    evidence = {
        23: 0, 
        24: 0, 
        22: 0, 
        21: 0, 
        20: 0, 
        18: 0
    }
    # evidence = {}
    numSamples = 1000

    W = BN.likelihoodWeighting_Query(query, evidence, numSamples)
    print(W)

    (G, sampleG) = BN.gibbsAsk_Query(query, evidence, numSamples)
    print(G)

    MH75 = BN.metropolisHasting_Query(query, evidence, numSamples, 0.75)
    print(MH75)
    
if __name__ == "__main__":
    main()