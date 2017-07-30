# coding: utf-8
import pandas as pd


def prepare_dataframe(list_bingobingo):
    """Prepare data for hangod prediction.

    :param list_bingobingo:
    :return:
    """
    serieses = [convert_bingobingo_to_series(bingobingo) for bingobingo in list_bingobingo]
    df = pd.DataFrame(serieses)
    df.columns = ['identity'] + ['number{}'.format(i) for i in range(1, 81)]
    return df


def convert_bingobingo_to_series(bingobingo):
    return pd.Series(
        [bingobingo.identity] + list(bingobingo.numbers.values())
    )


if __name__ == '__main__':
    from bingobingo_playground.pagegetter import PageGetter
    from bingobingo_playground.pageparser import PageParser

    g1 = PageGetter()
    content = g1.get()
    p1 = PageParser()
    l_bingobingo = p1.parse(content)
    result = prepare_hangod_data(l_bingobingo)
