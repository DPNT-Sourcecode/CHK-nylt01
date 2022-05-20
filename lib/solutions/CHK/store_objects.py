from enum import Enum, auto

pricingRules = [
        {'item': 'A', 'unitPrice': 50, 'special': [(5, 200), (3, 130)]}, 
        {'item': 'B', 'unitPrice': 30, 'special': [(2, 45)], 'bundle': {'requirement': {'E': 2, 'B': 1}, 'discount': 30}}, 
        {'item': 'C', 'unitPrice': 20}, 
        {'item': 'D', 'unitPrice': 15},
        {'item': 'E', 'unitPrice': 40, 'bundle': {'requirement': {'E': 2, 'B': 1}, 'discount': 30}}
        {'item': 'F', 'unitPrice': 10, 'special': [(3, 20)]}
    ]

class Products(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()


