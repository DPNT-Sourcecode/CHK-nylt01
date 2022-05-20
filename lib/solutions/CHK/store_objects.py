from enum import Enum, auto

pricingRules = [
        {'item': 'A', 'unitPrice': 50, 'special': [(5, 200), (3, 130)]}, 
        {'item': 'B', 'unitPrice': 30, 'special': [(2, 45)], 'bundle': {'requirement': {'E': 2, 'B': 1}, 'discount': 30}}, 
        {'item': 'C', 'unitPrice': 20}, 
        {'item': 'D', 'unitPrice': 15},
        {'item': 'E', 'unitPrice': 40, 'bundle': {'requirement': {'E': 2, 'B': 1}, 'discount': 30}},
        {'item': 'F', 'unitPrice': 10, 'special': [(3, 20)]},
        {'item': 'G', 'unitPrice': 20},
        {'item': 'H', 'unitPrice': 10, 'special': [(10, 80), (5, 45)]},
        {'item': 'I', 'unitPrice': 35},
        {'item': 'J', 'unitPrice': 60},
        {'item': 'K', 'unitPrice': 80, 'special': [(2, 150)]},
        {'item': 'L', 'unitPrice': 90},
        {'item': 'M', 'unitPrice': 15, 'bundle': {'requirement': {'N': 3, 'M': 1}, 'discount': 15}},
        {'item': 'N', 'unitPrice': 40, 'bundle': {'requirement': {'N': 3, 'M': 1}, 'discount': 15}},
        {'item': 'O', 'unitPrice': 10},
        {'item': 'P', 'unitPrice': 50, 'special': [(5, 200)]},
        {'item': 'Q', 'unitPrice': 30, 'special': [(3, 80)], 'bundle': {'requirement': {'R': 3, 'Q': 1}, 'discount': 30}},
        {'item': 'R', 'unitPrice': 50, 'bundle': {'requirement': {'R': 3, 'Q': 1}, 'discount': 30}},
        {'item': 'S', 'unitPrice': 30},
        {'item': 'T', 'unitPrice': 20},
        {'item': 'U', 'unitPrice': 40, 'special': [(4, 120)]},
        {'item': 'V', 'unitPrice': 50, 'special': [(3, 130), (2, 90)]},
        {'item': 'W', 'unitPrice': 20},
        {'item': 'X', 'unitPrice': 90},
        {'item': 'Y', 'unitPrice': 10},
        {'item': 'Z', 'unitPrice': 50}
    ]

class Products(Enum):
    @classmethod
    def keys(cls) -> list:
        """Returns a list of all the enum keys."""
        return cls._member_names_

    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
    G = auto()
    H = auto()
    I = auto()
    J = auto()
    K = auto()
    L = auto()
    M = auto()
    N = auto()
    O = auto()
    P = auto()
    Q = auto()
    R = auto()
    S = auto()
    T = auto()
    U = auto()
    V = auto()
    W = auto()
    X = auto()
    Y = auto()
    Z = auto()



