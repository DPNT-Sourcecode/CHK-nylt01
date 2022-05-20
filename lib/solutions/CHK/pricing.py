from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
import math

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
            specialOffersToApply = self.quantity // specialQuantity
            runningtotal += specialOffersToApply * specialPrice
            #each item can only partake in a single special offer
            self.quantity -= specialOffersToApply * specialQuantity

        #remaining items priced normally
        runningtotal += self.quantity * self.unitPrice
        
        return runningtotal

class BundlePricer(Pricer):
    def __init__(self, item:str, unitPrice:int, bundle:dict, specialOffers:List[tuple]=None) -> None:
        self.item = item
        self.unitPrice = unitPrice
        self.specialOffers = specialOffers
        self.bundle = bundle
        self.quantity = 0

    def increment(self) -> None:
        self.quantity += 1
    
    def total(self, bundleBasket:dict) -> Tuple[int, List[str]]: 
        runningtotal = 0
        
        requirements = self.bundle['requirement']
        freeItems = math.inf
        for key, value in requirements.items():
            multiples = bundleBasket[key] // value
            if multiples < freeItems:
                freeItems = multiples

        if freeItems > 0:
            bundleBasketUpdated = {key: bundleBasket[key] - requirements.get(key, 0) * freeItems for key in bundleBasket}
            runningtotal -= self.bundle['discount']
        
        if self.specialOffers:
            itemsForSpecialOffer = bundleBasketUpdated[self.item]
            for specialQuantity, specialPrice in self.specialOffers:
                specialOffersToApply = itemsForSpecialOffer // specialQuantity
                runningtotal += specialOffersToApply * specialPrice
                #each item can only partake in a single special offer
                self.quantity -= specialOffersToApply * specialQuantity
            runningtotal += self.quantity * self.unitPrice
        else:
            runningtotal += self.quantity * self.unitPrice

        return runningtotal, bundleBasketUpdated

class PricerFactory():
    def get_pricers(self, pricingRules:List[dict]) -> Dict[str, Pricer]:
        new_pricingRules = dict()
        for ruleset in pricingRules:
            if 'bundle' and 'special' in ruleset:
                new_pricingRules[ruleset['item']] = BundlePricer(ruleset['item'], ruleset['unitPrice'], ruleset['bundle'], ruleset['special'])
            elif 'bundle' in ruleset:
                new_pricingRules[ruleset['item']] = BundlePricer(ruleset['item'], ruleset['unitPrice'], ruleset['bundle'])               
            elif 'special' in ruleset:
                new_pricingRules[ruleset['item']] = SpecialPricer(ruleset['unitPrice'], ruleset['special'])              
            else:
                new_pricingRules[ruleset['item']] = SimplePricer(ruleset['unitPrice'])
                
        
        return new_pricingRules


