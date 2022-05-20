import teller

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0

    for letter in skus:
        if letter not in ['A', 'B', 'C', 'D', 'E']:
            return -1

    pricingRules = [
            {'item': 'A', 'unitPrice': 50, 'special': [(5, 200), (3, 130)]}, 
            {'item': 'B', 'unitPrice': 30, 'special': [(2, 45)], 'bundle': {'requirement': 'EE', 'free': 'B'}}, 
            {'item': 'C', 'unitPrice': 20}, 
            {'item': 'D', 'unitPrice': 15},
            {'item': 'E', 'unitPrice': 40, 'bundle': {'requirement': {'E': 2}, 'free': 'B'}}
        ]
    
    checkoutInstance = teller.Checkout(pricingRules)

    runningtotal = checkoutInstance.calculate_total(skus)

    return runningtotal


