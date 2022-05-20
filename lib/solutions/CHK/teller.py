import pricing
from typing import List

class Checkout:
    def __init__(self, pricingRules:List[dict]):
        self.pricers = pricing.PricerFactory().get_pricers(pricingRules)
        self.bundleBasket = []

    def add_item(self, item:str) -> None:
        self.bundleBasket.append((item, self.pricers[item].unitPrice))
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