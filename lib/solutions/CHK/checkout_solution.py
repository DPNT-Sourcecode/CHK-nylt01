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
            {'item': 'A', 'unitPrice': 50, 'special': {1: {'specialQuantity': 5, 'specialPrice': 200}, 2:{'specialQuantity': 3, 'specialPrice': 130}}}, 
            {'item': 'B', 'unitPrice': 30, 'special': {'specialQuantity': 2, 'specialPrice': 45}}, 
            {'item': 'C', 'unitPrice': 20}, 
            {'item': 'D', 'unitPrice': 15},
            {'item': 'E', 'unitPrice': 40, 'bundle': 'EEB'}
        ]
    
    checkoutInstance = teller.Checkout(pricingRules)

    runningtotal = checkoutInstance.calculate_total(skus)

    return runningtotal


