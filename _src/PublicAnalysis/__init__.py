from .set_init import set_init
from .select_month import select_month


class PublicAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path


PublicAnalysis.set_init = set_init
PublicAnalysis.select_month = select_month
