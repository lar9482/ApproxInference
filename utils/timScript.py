import random
def tim_polytree(num_nodes, prob=0.5, max_parents=None):
    print(max_parents)
    edges = []
    clusters = []
    net = {}
    parent_net = {}
    # clusters start out as [[0],[1],[2],...,[num_nodes-1]]
    for i in range(num_nodes):
        clusters.append([i])
        net[i] = []
        parent_net[i] = []
    # While there are more than 2 clusters, randomly choose 2
    # and 2 nodes from those and create an edge between them
    # if it does not violate the max parent rule
    while len(clusters) > 1:
        c1 = clusters.pop(random.randint(0,len(clusters)-1))
        c2 = clusters.pop(random.randint(0,len(clusters)-1))
        e1 = c1[random.randint(0,len(c1)-1)] #source
        e2 = c2[random.randint(0,len(c2)-1)] #sink
        if len(net[e2]) < max_parents:
            edges.append([e1,e2])
            net[e2].append(e1)
            parent_net[e1].append(e2) # keeps list of this node's children
            clusters.append(c1+c2)
        else:
            clusters.append(c1)
            clusters.append(c2)
    print(net)
    print(parent_net)
    return net