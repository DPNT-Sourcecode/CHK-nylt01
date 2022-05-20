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
    
    tellerInstance = teller.Teller(store_objects.pricingRules, store_objects.bundleDict, store_objects.groupDict)

    runningtotal = tellerInstance.calculate_total(skus)

    return runningtotal



