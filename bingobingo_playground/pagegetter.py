#coding: utf-8
import re
import requests
from bs4 import BeautifulSoup

calendar_pattern = re.compile(r"(?<=Calendar2',')(\d{4})")


class PageGetter:
    """PageGetter

    Get bingo bingo source page
    """
    URL = "http://www.taiwanlottery.com.tw/lotto/BINGOBINGO/drawing.aspx"
    FORM_KEY_EVENTTARGET = '__EVENTTARGET'
    FORM_VAL_EVENTTARGET = 'Calendar2'
    FORM_KEY_VIEWSTATE = '__VIEWSTATE'
    FORM_KEY_EVENTTARGETARGUMENT = '__EVENTARGUMENT'
    FORM_KEY_VIEWSTATEGENERATOR = '__VIEWSTATEGENERATOR'
    FORM_KEY_EVENTVALIDATION = '__EVENTVALIDATION'

    def __init__(self):
        self._current_view_state = None
        self._current_eventtargetargument = None
        self._current_viewstategenerator = None
        self._current_eventvalidation = None

    def go(self, target_argument):
        if self._current_eventtargetargument is None:
            raise ValueError('Current view state is None. Please call get() method first.')
        self._current_eventtargetargument = target_argument

    def go_previous(self):
        if self._current_eventtargetargument is not None:
            self._current_eventtargetargument -= 1

    def get(self):
        """
        get current bingo bingo page

        :return:
        """
        if self._current_view_state is None:
            res = requests.get(self.URL)
            soup = BeautifulSoup(res.text, 'html.parser')
            self._current_view_state = soup.find('input', attrs={'name': self.FORM_KEY_VIEWSTATE}).attrs['value']
            self._current_eventtargetargument = int(calendar_pattern.findall(res.text)[-1])
            self._current_viewstategenerator = soup.find('input', attrs={'name': self.FORM_KEY_VIEWSTATEGENERATOR}).attrs['value']
            self._current_eventvalidation = soup.find('input', attrs={'name': self.FORM_KEY_EVENTVALIDATION}).attrs['value']
        else:
            res = requests.post(self.URL, data={
                self.FORM_KEY_EVENTTARGET: self.FORM_VAL_EVENTTARGET,
                self.FORM_KEY_EVENTTARGETARGUMENT: self._current_eventtargetargument,
                self.FORM_KEY_VIEWSTATE: self._current_view_state,
                self.FORM_KEY_VIEWSTATEGENERATOR: self._current_viewstategenerator,
                self.FORM_KEY_EVENTVALIDATION: self._current_eventvalidation
            })
        return res.text

if __name__ == '__main__':
    p1 = PageGetter()
