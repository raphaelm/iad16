from tsplib import TspFile, TspType, EdgeWeightType, DisplayDataType, Node2D


def test_read_tsp_file():
    with open('data/gr96.tsp') as f:
        tsp = TspFile.create_from_file(f)

    assert tsp.NAME == "gr96"
    assert tsp.COMMENT == "Africa-Subproblem of 666-city TSP (Groetschel)"
    assert tsp.TYPE == TspType.TSP
    assert tsp.DIMENSION == 96
    assert tsp.EDGE_WEIGHT_TYPE == EdgeWeightType.GEO
    assert tsp.DISPLAY_DATA_TYPE == DisplayDataType.COORD_DISPLAY
    assert len(tsp.nodes) == 96
    assert tsp.nodes[0] == Node2D(num=1, x=14.55, y=-23.31)


def test_read_tour_file():
    with open('data/gr96.opt.tour') as f:
        tsp = TspFile.create_from_file(f)

    assert tsp.NAME == "gr96.opt.tour"
    assert tsp.COMMENT == "Optimal tour for gr96 (55209)"
    assert tsp.TYPE == TspType.TOUR
    assert tsp.DIMENSION == 96
    assert len(tsp.tours) == 1
    assert len(tsp.tours[0]) == 96
    assert tsp.tours[0][:5] == [29, 2, 3, 4, 5]
    assert tsp.tours[0][-5:] == [36, 32, 31, 30, 1]
