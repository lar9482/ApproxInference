from BayesNet.loadBayesNet import loadInBayesNet

def main():
    
    test = loadInBayesNet('./Reference/polytree50.json')
    order = test.getTopologicalOrder()
    print()

if __name__ == "__main__":
    main()