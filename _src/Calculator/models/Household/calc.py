import numpy as np
from ...common.rate import ENV, FUEL


@property
def basic(self):
    _basics = self.BASIC[self.steps != 0]
    return _basics.max()


@property
def elec_rate(self):
    return np.floor((self.ELEC * self.steps).sum())


@property
def env(self):
    return np.floor(self.kwh * ENV)


@property
def fuel(self):
    return np.floor(self.kwh * FUEL)


@property
def elec_bill(self):
    _elec_bill = self.basic + self.elec_rate + self.env + self.fuel - self.guarantee
    if _elec_bill < 1000:
        return 1000
    else:
        return _elec_bill


@property
def guarantee(self):
    if self.kwh <= 200:
        if self.contract == "종합":
            return 4000
        elif self.contract == "단일":
            return 2500
    else:
        return 0
