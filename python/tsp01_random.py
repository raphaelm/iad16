import sys
import numpy as np

import tsplib
import matplotlib.pyplot as plt


def generate_random_tours(problem, n=100):
    nodes = np.array([node.num for node in problem.nodes])
    for i in range(n):
        np.random.shuffle(nodes)
        yield nodes


with open(sys.argv[1]) as f:
    prob = tsplib.TspFile.create_from_file(f)


lengths = []
for tour in generate_random_tours(prob, 1000000):
    length = prob.length(tour)
    lengths.append(length)


# the histogram of the data
n, bins, patches = plt.hist(lengths, 50, facecolor='green')

plt.xlabel('Random tour length')
plt.ylabel('Number of tours')
plt.title("1'000'000 Random tours for {}".format(prob.NAME))
plt.grid(True)

plt.savefig(sys.argv[2])