from tsplib import TspFile


def test_gr96():
    with open('data/gr96.tsp') as f:
        prob = TspFile.create_from_file(f)
    with open('data/gr96.opt.tour') as f:
        tour = TspFile.create_from_file(f)

    assert prob.length(tour.tours[0]) == 55209


def test_pcb442():
    with open('data/pcb442.tsp') as f:
        prob = TspFile.create_from_file(f)
    with open('data/pcb442.opt.tour') as f:
        tour = TspFile.create_from_file(f)

    assert prob.length(tour.tours[0]) == 50778
