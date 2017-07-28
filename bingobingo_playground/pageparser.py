# coding: utf-8
import re
from bingobingo_playground.bingobingo import BingoBingo

ROW_PATTERN = re.compile(r'(?<=>)(\d{9})(?=<).*?' + '(?:(\d{2})\s+)' * 20)


class PageParser:
    """Parse bingo bingo page

    """
    PARSER = 'html.parser'

    def parse(self, page_content):
        """Parse a bingo bingo page

        :param page_content: a bingo bingo page str. Usually comes from PageGetter
        :return: a list of BingoBingo object
        """
        result = []
        for row in ROW_PATTERN.findall(page_content):
            bingobingo = self._generate_bingobingo_from_row(row)
            result.append(bingobingo)
        return result

    def _generate_bingobingo_from_row(self, row):
        bingobingo = BingoBingo()
        bingobingo.identity = row[0]
        bingobingo.number1 = row[1]
        bingobingo.number2 = row[2]
        bingobingo.number3 = row[3]
        bingobingo.number4 = row[4]
        bingobingo.number5 = row[5]
        bingobingo.number6 = row[6]
        bingobingo.number7 = row[7]
        bingobingo.number8 = row[8]
        bingobingo.number9 = row[9]
        bingobingo.number10 = row[10]
        bingobingo.number11 = row[11]
        bingobingo.number12 = row[12]
        bingobingo.number13 = row[13]
        bingobingo.number14 = row[14]
        bingobingo.number15 = row[15]
        bingobingo.number16 = row[16]
        bingobingo.number17 = row[17]
        bingobingo.number18 = row[18]
        bingobingo.number19 = row[19]
        bingobingo.number20 = row[20]
        return bingobingo


if __name__ == '__main__':
    from bingobingo_playground.pagegetter import PageGetter
    g1 = PageGetter()
    content = g1.get()
    p1 = PageParser()
    result = p1.parse(content)
