from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class Pricer(ABC):
    @abstractmethod
    def increment():
        pass

    @abstractmethod
    def total():
        pass

class SimplePricer(Pricer):
    def __init__(self, unitPrice:int) -> None:
        self.unitPrice = unitPrice
        self.quantity = 0
    
    def increment(self) -> None:
        self.quantity += 1

    def total(self) -> int:
        return self.quantity * self.unitPrice

class SpecialPricer(Pricer):
    def __init__(self, unitPrice:int, specialOffers:List[tuple]) -> None:
        self.unitPrice = unitPrice
        self.specialOffers = specialOffers
        self.quantity = 0

    def increment(self) -> None:
        self.quantity += 1
    
    def total(self) -> int:
        runningtotal = 0

        for specialQuantity, specialPrice in self.specialOffers:
            offersToApply = self.quantity // specialQuantity
            runningtotal += offersToApply * specialPrice
            #each item can only partake in a single special offer
            self.quantity -= offersToApply * specialQuantity

        #remaining items priced normally
        runningtotal += self.quantity * self.unitPrice
        
        return runningtotal

class BundlePricer(Pricer):
    def __init__(self, item:str, unitPrice:int, bundleQuantity:int, bundleItems:list) -> None:
        self.item = item
        self.unitPrice = unitPrice
        self.bundleQuantity = bundleQuantity
        self.bundleItems = bundleItems
        self.quantity = 0

    def increment(self) -> None:
        self.quantity += 1
    
    def total(self, bundleBasket:List[Tuple]) -> Tuple[int, List[Tuple]]: 
        runningtotal = 0
        
        relevantBasketItems = [item for item in bundleBasket if item[0] in self.bundleItems]
        irrelevantBasketItems = [item for item in bundleBasket if item[0] not in self.bundleItems]

        freeItems = len(relevantBasketItems) // self.bundleQuantity
        if freeItems > 0:
            relevantBasketItemsSorted = sorted(relevantBasketItems, key=lambda x: x[1])
            runningtotal -= sum(tuple[1] for tuple in relevantBasketItemsSorted[0:freeItems])

            #each bundle consists of one cheap item and rest expensive items
            del relevantBasketItemsSorted[0:freeItems]
            del relevantBasketItemsSorted[- (self.bundleQuantity * freeItems - freeItems):]

            bundleBasket = relevantBasketItemsSorted + irrelevantBasketItems
            
        runningtotal += self.quantity * self.unitPrice

        return runningtotal, bundleBasket

class PricerFactory():
    def get_pricers(self, pricingRules:List[dict]) -> Dict[str, Pricer]:
        new_pricingRules = dict()
        for ruleset in pricingRules:
            if 'bundle' in ruleset:
                new_pricingRules[ruleset['item']] = BundlePricer(ruleset['item'], ruleset['unitPrice'], ruleset['bundle']['quantity'], ruleset['bundle']['items'])               
            elif 'special' in ruleset:
                new_pricingRules[ruleset['item']] = SpecialPricer(ruleset['unitPrice'], ruleset['special'])              
            else:
                new_pricingRules[ruleset['item']] = SimplePricer(ruleset['unitPrice'])
                
        
        return new_pricingRules

