import sys

import matplotlib.pyplot as plt

import tsplib
from tsp02a_nextneighbor import next_neighbor_tour

with open(sys.argv[1]) as f:
    prob = tsplib.TspFile.create_from_file(f)

startnodes = []
lengths = []
for n in prob.nodes:
    lengths.append(prob.length(next_neighbor_tour(prob, n.num)))
    startnodes.append(n.num)
    print(n.num)

# the histogram of the data

plt.plot(startnodes, lengths)

plt.xlabel('Starting point')
plt.ylabel('Tour length')
plt.title('Various NN starting points for {}'.format(prob.NAME))
plt.grid(True)

plt.savefig(sys.argv[2])
