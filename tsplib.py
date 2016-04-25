import string
from collections import namedtuple
from enum import Enum


class TspType(Enum):
    TSP = 1
    ATSP = 2
    SOP = 3
    HCP = 4
    CVRP = 5
    TOUR = 6


class EdgeWeightType(Enum):
    EXPLICIT = 1
    EUC_2D = 2
    EUC_3D = 3
    MAX_2D = 4
    MAX_3D = 5
    MAN_2D = 6
    MAN_3D = 7
    CEIL_2D = 8
    GEO = 9
    ATT = 10
    XRAY1 = 11
    XRAY2 = 12
    SPECIAL = 13


class EdgeWeightFormat(Enum):
    FUNCTION = 1
    FULL_MATRIX = 2
    UPPER_ROW = 3
    LOWER_ROW = 4
    UPPER_DIAG_ROW = 5
    LOWER_DIAG_ROW = 6
    UPPER_COL = 7
    LOWER_COL = 8
    UPPER_DIAG_COL = 9
    LOWER_DIAG_COL = 10


class EdgeDataFormat(Enum):
    EDGE_LIST = 1
    ADJ_LIST = 2


class NodeCoordType(Enum):
    TWOD_COORDS = 1
    THREED_COORDS = 2
    NO_COORDS = 3


class DisplayDataType(Enum):
    COORD_DISPLAY = 1
    TWOD_DISPLAY = 2
    NO_DISPLAY = 3


Node2D = namedtuple('Node2D', ('num', 'x', 'y'))
Node3D = namedtuple('Node3D', ('num', 'x', 'y', 'z'))


class TspFile:
    NAME = None
    TYPE = None
    COMMENT = None
    DIMENSION = None
    CAPACITY = None
    EDGE_WEIGHT_TYPE = None
    EDGE_WEIGHT_FORMAT = None
    EDGE_DATA_FORMAT = None
    NODE_COORD_TYPE = NodeCoordType.NO_COORDS
    DISPLAY_DATA_TYPE = None

    def __init__(self):
        self.nodes = []
        self.tours = []

    def _parse_specification_line(self, key, value):
        if key in ('DIMENSION', 'CAPACITY'):
            value = int(value)
        elif key == 'TYPE':
            value = TspType[value]
        elif key == 'EDGE_WEIGHT_TYPE':
            value = EdgeWeightType[value]
        elif key == 'EDGE_WEIGHT_FORMAT':
            value = EdgeWeightFormat[value]
        elif key == 'EDGE_DATA_FORMAT':
            value = EdgeDataFormat[value]
        elif key == 'NODE_COORD_TYPE':
            value = NodeCoordType[value]
        elif key == 'DISPLAY_DATA_TYPE':
            value = DisplayDataType[value]

        setattr(self, key, value)

    @classmethod
    def create_from_file(cls, filelike):
        obj = cls()

        parser_state = 'specification'

        for line in filelike:
            line = line.strip()
            if line == 'EOF':
                break

            if parser_state == 'specification':
                if ':' in line:
                    key, value = line.split(':')
                    obj._parse_specification_line(key.strip(), value.strip())
                    continue
                else:
                    parser_state = 'data'

            if line[0] in string.ascii_letters:
                # This is the beginning of a new section
                if line == 'NODE_COORD_SECTION':
                    parser_state = 'nodes'
                elif line == 'TOUR_SECTION':
                    parser_state = 'tours'
                else:
                    raise ValueError('The data section "{}" is not yet supported'.format(line))
            else:
                # This is data content
                if parser_state == 'nodes':
                    parts = line.split(' ')
                    if len(parts) == 4:
                        node = Node3D(num=int(parts[0]), x=float(parts[1]), y=float(parts[2]), z=float(parts[3]))
                    elif len(parts) == 3:
                        node = Node2D(num=int(parts[0]), x=float(parts[1]), y=float(parts[2]))
                    else:
                        raise ValueError('Unknown coordinate type')
                    obj.nodes.append(node)
                elif parser_state == 'tours':
                    node = int(line)
                    if node == -1 or not obj.tours:
                        obj.tours.append([])
                    if node != -1:
                        obj.tours[-1].append(node)
                else:
                    raise ValueError('Encountered data in unsupported parser state state.')

        # Clean up left-over empty lists from parser
        if obj.tours and not obj.tours[-1]:
            obj.tours = obj.tours[:-1]

        # Default values
        if not obj.DISPLAY_DATA_TYPE:
            obj.DISPLAY_DATA_TYPE = DisplayDataType.COORD_DISPLAY if obj.nodes else DisplayDataType.NO_DISPLAY

        return obj