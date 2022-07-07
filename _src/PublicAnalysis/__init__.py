from .set_init import set_init
from .set_calc import set_calc
from .select_month import select_month


class PublicAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path


PublicAnalysis.set_init = set_init
PublicAnalysis.set_calc = set_calc
PublicAnalysis.select_month = select_month
