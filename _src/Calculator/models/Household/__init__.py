from .set_rate import set_rate
from .calc import basic, elec_rate, env, fuel, guarantee, elec_bill


class Household:
    def __init__(self, name, kwh):
        self.name = name
        self.kwh = kwh


Household.set_rate = set_rate
Household.basic = basic
Household.elec_rate = elec_rate
Household.env = env
Household.fuel = fuel
Household.guarantee = guarantee
Household.elec_bill = elec_bill
