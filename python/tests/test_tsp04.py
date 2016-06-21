from tsplib import TspFile
from tsp04_modifications import nodelinks_from_tour, tour_from_nodelinks, move_node, move_2opt, print_nodelinks


def test_conv_roundtrip():
    with open('data/gr96.tsp') as f:
        prob = TspFile.create_from_file(f)
    with open('data/gr96.opt.tour') as f:
        tour = TspFile.create_from_file(f)

    assert tour_from_nodelinks(nodelinks_from_tour(prob, tour.tours[0])) == tour.tours[0]


def test_move_node():
    with open('data/gr96.tsp') as f:
        prob = TspFile.create_from_file(f)
    first = nodelinks_from_tour(prob, [1, 2, 3, 4, 5])
    two = first.next
    three = first.next.next
    move_node(two, three)
    assert tour_from_nodelinks(first) == [1, 3, 2, 4, 5]
    move_node(two, first)
    assert tour_from_nodelinks(first) == [1, 2, 3, 4, 5]


def test_move_2opt():
    with open('data/gr96.tsp') as f:
        prob = TspFile.create_from_file(f)
    first = nodelinks_from_tour(prob, [1, 2, 3, 4, 5])
    two = first.next
    three = first.next.next
    four = first.next.next.next
    move_2opt(two, four)
    assert tour_from_nodelinks(first) == [1, 2, 4, 3, 5]
    move_2opt(two, three)
    assert tour_from_nodelinks(first) == [1, 2, 3, 4, 5]
