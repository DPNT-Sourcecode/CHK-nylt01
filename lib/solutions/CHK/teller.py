from . import pricing
from collections import defaultdict
from typing import List

class Teller:
    def __init__(self, pricingRules:List[dict]):
        self.pricers = pricing.PricerFactory().get_pricers(pricingRules)
        self.bundleBasket = defaultdict(int)

    def add_item(self, item:str) -> None:
        self.bundleBasket[item] += 1
        self.pricers[item].increment()
    
    def calculate_total(self, skus:str) -> int:
        for item in skus:
            self.add_item(item)

        runningTotal = 0
        for pricer in self.pricers.values():
            if isinstance(pricer, pricing.BundlePricer): 
                total, self.bundleBasket = pricer.total(self.bundleBasket)
                runningTotal += total
            else:
                runningTotal += pricer.total()

        return runningTotal