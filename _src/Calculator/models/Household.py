from .set_rate import set_rate


class Household:
    def __init__(self, name, kwh):
        self.name = name
        self.kwh = kwh


Household.set_rate = set_rate
