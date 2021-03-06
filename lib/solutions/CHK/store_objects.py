from enum import Enum, auto

pricingRules = [
        {'item': 'A', 'unitPrice': 50, 'special': [(5, 200), (3, 130)]}, 
        {'item': 'B', 'unitPrice': 30, 'special': [(2, 45)], 'bundleID': 1}, 
        {'item': 'C', 'unitPrice': 20}, 
        {'item': 'D', 'unitPrice': 15},
        {'item': 'E', 'unitPrice': 40, 'bundleID': 1},
        {'item': 'F', 'unitPrice': 10, 'special': [(3, 20)]},
        {'item': 'G', 'unitPrice': 20},
        {'item': 'H', 'unitPrice': 10, 'special': [(5, 45), (10, 80)]},
        {'item': 'I', 'unitPrice': 35},
        {'item': 'J', 'unitPrice': 60},
        {'item': 'K', 'unitPrice': 70, 'special': [(2, 120)]},
        {'item': 'L', 'unitPrice': 90},
        {'item': 'M', 'unitPrice': 15, 'bundleID': 2},
        {'item': 'N', 'unitPrice': 40, 'bundleID': 2},
        {'item': 'O', 'unitPrice': 10},
        {'item': 'P', 'unitPrice': 50, 'special': [(5, 200)]},
        {'item': 'Q', 'unitPrice': 30, 'special': [(3, 80)], 'bundleID': 3},
        {'item': 'R', 'unitPrice': 50, 'bundleID': 3},
        {'item': 'S', 'unitPrice': 20, 'groupID': 1},
        {'item': 'T', 'unitPrice': 20, 'groupID': 1},
        {'item': 'U', 'unitPrice': 40, 'special': [(4, 120)]},
        {'item': 'V', 'unitPrice': 50, 'special': [(2, 90), (3, 130)]},
        {'item': 'W', 'unitPrice': 20},
        {'item': 'X', 'unitPrice': 17, 'groupID': 1},
        {'item': 'Y', 'unitPrice': 20, 'groupID': 1},
        {'item': 'Z', 'unitPrice': 21, 'groupID': 1}
    ]

bundleDict = {
    1: {'requirement': {'E': 2, 'B': 1}, 'discount': 30},
    2: {'requirement': {'N': 3, 'M': 1}, 'discount': 15},
    3: {'requirement': {'R': 3, 'Q': 1}, 'discount': 30}
}

groupDict = {
    1: {'groupMembers': 'STXYZ', 'groupQuantity': 3, 'groupPrice': 45}
}

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


