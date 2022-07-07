from .BillTable import BillTable
from .set_init import set_init
from .set_calc import set_calc
from .select_month import select_month


class PublicAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path

    def set(self,
            start_kwh=0,
            end_kwh=250,
            start_percentage=10,
            end_percentage=40,
            basic_percentage=30):
        self.bill_table = BillTable(
            analyzer=self, public_percentage=basic_percentage)


PublicAnalysis.set_init = set_init
PublicAnalysis.set_calc = set_calc
PublicAnalysis.select_month = select_month
