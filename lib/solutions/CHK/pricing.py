from abc import ABC, abstractmethod
from email.policy import default
from tokenize import group
from typing import Dict, List, Tuple
from collections import defaultdict, Counter
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
        self.specialOffers = sorted(specialOffers, key=lambda x: x[1], reverse=True) #apply biggest offer first
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
    
    def total(self, sharedBasket:defaultdict) -> Tuple[int, defaultdict]: 
        runningtotal = 0
        
        requirements = self.bundle['requirement']
        freeItems = math.inf
        for key, value in requirements.items():
            multiples = sharedBasket[key] // value
            if multiples < freeItems:
                freeItems = multiples

        if freeItems > 0:
            sharedBasket = {key: sharedBasket[key] - requirements.get(key, 0) * freeItems for key in sharedBasket}
            sharedBasket = defaultdict(int, sharedBasket) 
            runningtotal -= self.bundle['discount'] * freeItems
        
        if self.specialOffers:
            itemsForSpecialOffer = sharedBasket[self.item]
            for specialQuantity, specialPrice in self.specialOffers:
                specialOffersToApply = itemsForSpecialOffer // specialQuantity
                runningtotal += specialOffersToApply * specialPrice
                #each item can only partake in a single special offer
                self.quantity -= specialOffersToApply * specialQuantity
            runningtotal += self.quantity * self.unitPrice
        else:
            runningtotal += self.quantity * self.unitPrice

        return runningtotal, sharedBasket

class GroupPricer(Pricer):
    def __init__(self, item:str, unitPrice:int, groupInfo:dict, productUnitPrices:dict) -> None:
        self.item = item
        self.unitPrice = unitPrice
        self.quantity = 0
        self.groupInfo = groupInfo
        self.productUnitPrices = productUnitPrices

    def increment(self) -> None:
        self.quantity += 1

    def total(self, sharedBasket:defaultdict) -> Tuple[int, defaultdict]:
        runningtotal = 0
        groupItems = [i for i in sharedBasket for j in range(sharedBasket[i]) if i in self.groupInfo['groupMembers']]
        completeGroups = len(groupItems) // self.groupInfo['groupQuantity']

        if completeGroups > 0:
            groupItemsPriceSortedHighLow = sorted(groupItems, key = lambda x: self.productUnitPrices[x], reverse = True)

            #calculate actual price of removed items and apply discount
            actualPrice = sum(self.productUnitPrices[item] for item in groupItemsPriceSortedHighLow[0 : completeGroups * self.groupInfo['groupQuantity']])
            runningtotal -= (actualPrice - self.groupInfo['groupPrice'])

            #update sharedBasket
            del groupItemsPriceSortedHighLow[0 : completeGroups * self.groupInfo['groupQuantity']]
            sharedBasket = defaultdict(int)
            for item in groupItemsPriceSortedHighLow:
                sharedBasket[item] = sharedBasket.get(item, 0) +1

        runningtotal += self.quantity * self.unitPrice

        
        return runningtotal, sharedBasket

class PricerFactory():
    def get_pricers(self, pricingRules:List[dict]) -> Dict[str, Pricer]:
        newPricingRules = dict()
        productUnitPrices = {ruleset['item']: ruleset['unitPrice'] for ruleset in pricingRules}

        for ruleset in pricingRules:
            if all(key in ruleset for key in('bundle', 'special')):
                newPricingRules[ruleset['item']] = BundlePricer(ruleset['item'], ruleset['unitPrice'], ruleset['bundle'], ruleset['special'])
            elif 'bundle' in ruleset:
                newPricingRules[ruleset['item']] = BundlePricer(ruleset['item'], ruleset['unitPrice'], ruleset['bundle'])               
            elif 'special' in ruleset:
                newPricingRules[ruleset['item']] = SpecialPricer(ruleset['unitPrice'], ruleset['special'])     
            elif 'group' in ruleset:
                newPricingRules[ruleset['item']] = GroupPricer(ruleset['item'], ruleset['unitPrice'], ruleset['group'], productUnitPrices)         
            else:
                newPricingRules[ruleset['item']] = SimplePricer(ruleset['unitPrice'])
            

        
        return newPricingRules

