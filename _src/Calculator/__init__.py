
from _src.Calculator.common.get_season_kr import get_season_kr

from .set_households import set_households


class Calculator:
    def __init__(self, datas, month, contract="단일"):
        if contract != "단일" and contract != "종합":
            raise ValueError("only 단일 or 종합")
        self.datas = datas
        self.contract = contract
        self.season = get_season_kr(month)


Calculator.set_households = set_households
