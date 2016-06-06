import sys
from math import floor

import tsplib


def quicksort(seq, key=lambda s: s):
    """
    Iteratives QuickSort entsprechend Skript Seite 39
    """
    stack = []
    n = len(seq)
    stack.append(0)
    stack.append(n - 1)

    while stack:
        r, l = stack.pop(), stack.pop()
        if l < r:
            v = key(seq[r])
            i = l - 1
            j = r
            while True:
                while True:
                    i += 1
                    if i >= n or key(seq[i]) >= v:
                        break
                while True:
                    j -= 1
                    if j < 0 or key(seq[j]) <= v:
                        break
                if j > i:
                    seq[i], seq[j] = seq[j], seq[i]
                else:
                    seq[i], seq[r] = seq[r], seq[i]
                    break
            if i - 1 <= r - i:
                stack.append(i + 1)
                stack.append(r)
                stack.append(l)
                stack.append(i - 1)
            else:
                stack.append(l)
                stack.append(i - 1)
                stack.append(i + 1)
                stack.append(r)
    return seq


def project(x, y, minx, miny, maxx, maxy):
    """
    Umkehrfunktion einer Space-Filling-Courve. Projeziert (x,y) auf [0,1]
    """
    iq = [0] * 12
    kx = floor((x - minx) / ((maxx - minx) * 0.501 / 1024))
    ky = floor((y - miny) / ((maxy - miny) * 0.501 / 1024))

    for j in range(1, 12):
        jx = floor(kx / 1024)
        jy = floor(ky / 1024)
        kx = 2 * (kx - 1024 * jx)
        ky = 2 * (ky - 1024 * jy)
        iq[j] = jy + 3 * jx - 2 * jx * jy

    t = iq[11] / 4
    for j in range(10, 0, -1):
        t += (6 - iq[j]) / 4
        t -= floor(t)
        t = (3.5 + t + iq[j]) / 4
    return t - floor(t)


def spacefilling_tour(problem):
    minx = min(n.x for n in problem.nodes)
    miny = min(n.y for n in problem.nodes)
    maxx = max(n.x for n in problem.nodes)
    maxy = max(n.y for n in problem.nodes)
    tour = []
    for n in problem.nodes:
        tour.append((n.num, project(n.x, n.y, minx, miny, maxx, maxy)))
    quicksort(tour, key=lambda s: s[1])
    return [n[0] for n in tour]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        prob = tsplib.TspFile.create_from_file(f)

    tour = spacefilling_tour(prob)
    length = prob.length(tour)
    print("Tour: %r\nLength: %d" % (tour, length))
