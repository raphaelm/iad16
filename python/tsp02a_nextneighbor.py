import sys

import tsplib


def next_neighbor_tour(problem, startnode=1):
    nodes_unvisited = list(problem.nodes)
    startnode = problem.nodes[startnode - 1]
    tour = [startnode]
    nodes_unvisited.remove(startnode)
    while nodes_unvisited:
        n = min(nodes_unvisited, key=lambda nd: problem.dist(tour[-1], nd))
        nodes_unvisited.remove(n)
        tour.append(n)
    return [n.num for n in tour]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        prob = tsplib.TspFile.create_from_file(f)

    tour = next_neighbor_tour(prob, 1)
    length = prob.length(tour)
    print("Tour: %r\nLength: %d" % (tour, length))
