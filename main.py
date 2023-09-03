from BayesNet.loadBayesNet import loadInBayesNet

def main():
    
    BN = loadInBayesNet('./Reference/polytree10.json')

    query = 5
    evidence = {
        0: 0,
        1: 0,
        4: 1,
        9: 0
    }
    numSamples = 500

    W = BN.likelihoodWeighting_Query(query, evidence, numSamples)
    print(W)
    
    G = BN.gibbsAsk_Query(query, evidence, numSamples)
    print(G)
    
if __name__ == "__main__":
    main()