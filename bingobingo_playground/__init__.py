#coding: utf-8
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from bingobingo_playground.pagegetter import PageGetter
from bingobingo_playground.pageparser import PageParser
from bingobingo_playground import data
from bingobingo_playground import hangod_predict


def predict_hangod():
    pg = PageGetter()
    recent_bingo_content = pg.get()
    pp = PageParser()
    list_bingobingo = pp.parse(recent_bingo_content)
    df = data.prepare_dataframe(list_bingobingo)
    features, labels = hangod_predict.prepare_hangod_features_labels(df)
    x_train, x_test, y_train, y_test = hangod_predict.prepare_train_test_data(features, labels)
    clf = hangod_predict.get_trained_clf(x_train, y_train)
    pred = clf.predict(x_test)
    cm = confusion_matrix(pred, y_test)
    print(cm)
    newest_row = features[:1]
    print(clf.predict(newest_row))
    # plot
    plt.imshow(cm, cmap=plt.cm.Blues)
    tick_marks = range(2)
    classes = ['False', 'True']
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.show()


if __name__ == '__main__':
    predict_hangod()
