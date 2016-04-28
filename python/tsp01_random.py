import random
import sys

import tsplib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def generate_random_tour(prob):
    nodes = [node.num for node in prob.nodes]
    random.shuffle(nodes)
    return nodes


with open(sys.argv[1]) as f:
    prob = tsplib.TspFile.create_from_file(f)


lengths = []
for i in range(100000):
    tour = generate_random_tour(prob)
    length = prob.length(tour)
    lengths.append(length)


# the histogram of the data
n, bins, patches = plt.hist(lengths, 50, facecolor='green')

plt.xlabel('Random tour length')
plt.ylabel('Number of tours')
plt.title('Random tours for {}'.format(prob.NAME))
plt.grid(True)

plt.show()