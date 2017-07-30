# coding: utf-8
from collections import OrderedDict


class BingoBingo:
    """Represent a bingo bingo row

    """

    def __init__(self):
        self.identity = None
        self.numbers = OrderedDict.fromkeys(range(1, 81), False)
