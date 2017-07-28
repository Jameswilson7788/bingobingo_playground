#coding: utf-8
import requests


class PageGetter:
    """PageGetter

    Get bingo bingo source page
    """
    URL = "http://www.taiwanlottery.com.tw/lotto/BINGOBINGO/drawing.aspx"

    def get(self):
        """
        get current bingo bingo page

        :return:
        """
        res = requests.get(self.URL)
        return res.text

if __name__ == '__main__':
    p1 = PageGetter()