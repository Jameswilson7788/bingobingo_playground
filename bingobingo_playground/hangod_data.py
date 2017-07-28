# coding: utf-8
import pandas as pd


def prepare_hangod_data(list_bingobingo, filename="hangod.csv"):
    """Prepare data for hangod prediction.

    :param list_bingobingo:
    :return:
    """
    serieses = [convert_bingobingo_to_series(bingobingo) for bingobingo in list_bingobingo]
    df = pd.DataFrame(serieses)
    return df


def convert_bingobingo_to_series(bingobingo):
    return pd.Series(
        [bingobingo.identity,
         bingobingo.number1,
         bingobingo.number2,
         bingobingo.number3,
         bingobingo.number4,
         bingobingo.number5,
         bingobingo.number6,
         bingobingo.number7,
         bingobingo.number8,
         bingobingo.number9,
         bingobingo.number10,
         bingobingo.number11,
         bingobingo.number12,
         bingobingo.number13,
         bingobingo.number14,
         bingobingo.number15,
         bingobingo.number16,
         bingobingo.number17,
         bingobingo.number18,
         bingobingo.number19,
         bingobingo.number20]
    )


if __name__ == '__main__':
    from bingobingo_playground.pagegetter import PageGetter
    from bingobingo_playground.pageparser import PageParser

    g1 = PageGetter()
    content = g1.get()
    p1 = PageParser()
    l_bingobingo = p1.parse(content)
    result = prepare_hangod_data(l_bingobingo)
