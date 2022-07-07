from .Basic import Basic
from .BillTable import BillTable
from .set_init import set_init
from .set_calc import set_calc
from .select_month import select_month


class PublicAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path

    def set(self):
        self.basic = Basic(analyzer=self)

    def set_bill_table(self, public_percentage=30):
        self.bill_table = BillTable(
            analyzer=self, public_percentage=public_percentage)


PublicAnalysis.set_init = set_init
PublicAnalysis.set_calc = set_calc
PublicAnalysis.select_month = select_month
