import sys

import tsplib
from tsp02a_nextneighbor import next_neighbor_tour


class NodeLink:
    def __init__(self, node, next=None, prev=None):
        self.node = node
        self.next = next
        self.prev = prev

    def __eq__(self, other):
        return self.node == other.node

    def __repr__(self):
        return "<NodeLink node=%d next=%d prev=%d>" % (
            self.node.num,
            self.next.node.num if self.next else 'None',
            self.prev.node.num if self.prev else 'None'
        )


def nodelinks_from_tour(problem, tour):
    """
    Konvertiert eine Tourspezifikation des Formates aus tsplib.py (Liste mit Knotennummerierungen,
    z.B. [1,3,2,4] in eine Art verkettete Liste von Knoten, wobei die Klasse NodeLink zur Verkettung
    benutzt wird. Gibt einen Anfangsknoten zurück. Der letzte Knoten zeigt wieder auf den ersten Knoten
    als Nachfolger.
    """
    last = first = NodeLink(problem.nodes[tour[0] - 1])
    for t in tour[1:]:
        node = NodeLink(problem.nodes[t - 1])
        if last:
            last.next = node
            node.prev = last
        last = node
    last.next = first
    first.prev = last
    return first


def print_nodelinks(first):
    """
    Gibt eine Graphentour beginnend bei first auf der Kommandozeile aus (für Debugging)
    """
    cur = first
    print(first)
    while True:
        cur = cur.next
        if cur == first:
            break
        print("->", cur)


def tour_from_nodelinks(first):
    """
    Konvertiert eine Kette von NodeLink-Objekten in eine Liste von Knotennummern.
    """
    tour = []
    cur = first
    while True:
        tour.append(cur.node.num)
        cur = cur.next
        if cur == first:
            return tour


def move_node(subject, target):
    """
    Verschiebt den Knoten subjekt hinter target (Kernstück der Node-Insertion-Modifikation)
    """
    old_prev, old_next = subject.prev, subject.next
    old_prev.next, old_next.prev = old_next, old_prev
    target.next.prev = subject
    subject.next, subject.prev = target.next, target
    target.next = subject


def modify_node_insertion(problem, first):
    """
    Sucht nacht einer Node-Insertion-Modifikation, die die Tour verkürzt, führt diese durch
    und bricht dann ab.
    """
    original_length = problem.length(tour_from_nodelinks(first))  # O(n)
    cur = first
    while True:
        searchcur = cur.next

        while True:
            # Do modification, insert cur after searchcur
            old_prev = cur.prev
            move_node(cur, searchcur)

            length = problem.length(tour_from_nodelinks(cur))  # O(n)
            if length < original_length:
                print("Moving node %d after %d reduces length to %d" % (
                    cur.node.num, searchcur.node.num, length
                ))
                return True
            else:
                # Reverse modification
                move_node(cur, old_prev)

            searchcur = searchcur.next
            if searchcur == cur:
                break

        cur = cur.next
        if cur == first:
            return False


def reverse_direction(start, end):
    """
    Kehrt die Richtung aller Kanten auf dem Weg von start nach end um
    """
    cur = start.next
    last = start
    start.prev = cur

    while True:
        if cur == end:
            cur.next = last
            break
        n = cur.next
        cur.next, cur.prev = cur.prev, cur.next
        last = cur
        cur = n


def move_2opt(s1, s2):
    """
    Trennt die Kanten zwischen s1/s2 und ihren jeweiligen Nachfolgern und verbindet neu
    """
    a, b = s1.next, s2.next
    s1.next = s2
    s2.prev = s1
    reverse_direction(a, s2)  # O(n)
    a.next = b
    b.prev = a


def modify_2opt(problem, first):
    """
    Sucht nacht einer 2-Opt-Modifikation, die die Tour verkürzt, führt diese durch
    und bricht dann ab.
    """
    original_length = problem.length(tour_from_nodelinks(first))  # O(n)
    cur = first
    while True:
        searchcur = cur.next.next

        while True:
            # Do modification, insert cur after searchcur
            old_next = cur.next
            move_2opt(cur, searchcur)

            length = problem.length(tour_from_nodelinks(cur))  # O(n)
            if length < original_length:
                print("Removing edges after %d and %d and reconnecting reduces length to %d" % (
                    cur.node.num, searchcur.node.num, length
                ))
                return True
            else:
                # Reverse modification
                move_2opt(cur, old_next)

            searchcur = searchcur.next
            if searchcur == cur:
                break

        cur = cur.next
        if cur == first:
            return False


def modifications(problem, tour, heuristic):
    """
    Führt so lange Modifikationen nach der in heuristic gegebenen Funktion durch,
    bis es keine mehr gibt, die die Tour verkürzen würden.
    """
    first = nodelinks_from_tour(problem, tour)  # O(n)

    while heuristic(problem, first):
        # Probiere die Modifikation für alle Knoten durch. Wenn etwas modifiziert
        # wurde, beginne von vorne.
        pass

    return tour_from_nodelinks(first)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        prob = tsplib.TspFile.create_from_file(f)

    tour = next_neighbor_tour(prob, 1)
    tour = modifications(prob, tour, heuristic=modify_2opt)
    tour = modifications(prob, tour, heuristic=modify_node_insertion)
    length = prob.length(tour)
    print("Tour: %r\nLength: %d" % (tour, length))
