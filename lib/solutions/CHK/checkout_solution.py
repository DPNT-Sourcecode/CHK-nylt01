from . import teller
from . import store_objects


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0

    for product in skus:
        if product not in store_objects.Products.keys():
            return -1
    
    tellerInstance = teller.Teller(store_objects.pricingRules)

    runningtotal = tellerInstance.calculate_total(skus)

    return runningtotal

##CODE FOR TESTING
if __name__ == '__main__':
    print(checkout('EEEEBB'))



