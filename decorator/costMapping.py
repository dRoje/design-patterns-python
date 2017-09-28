from abc import ABCMeta
from beverage import Beverage


class CostMapping:
    __metaclass__ = ABCMeta
    costMap = {
        Beverage.TALL : .10,
        Beverage.GRANDE : .15,
        Beverage.VENTI : .20
    }

    @staticmethod
    def getCost(size):
        return CostMapping.costMap[size]


class MochaCostMapping(CostMapping):
    __metaclass__ = ABCMeta
    costMap = {
        Beverage.TALL: .12,
        Beverage.GRANDE: .16,
        Beverage.VENTI: .22
    }
