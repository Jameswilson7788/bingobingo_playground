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
        for number in row[1:]:
            bingobingo.numbers[int(number)] = True
        return bingobingo


if __name__ == '__main__':
    from bingobingo_playground.pagegetter import PageGetter
    g1 = PageGetter()
    content = g1.get()
    p1 = PageParser()
    result = p1.parse(content)
