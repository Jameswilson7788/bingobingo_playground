#coding: utf-8
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from bingobingo_playground.bingobingo import Session, BingoBingo
from bingobingo_playground.pagegetter import PageGetter
from bingobingo_playground.pageparser import PageParser
from bingobingo_playground import data
from bingobingo_playground import hangod_predict

def predict_hangod():
    # read bingobingo data from database
    session = Session()
    list_bingobingo = list(session.query(BingoBingo).order_by(BingoBingo.identity.desc()))
    df = data.prepare_dataframe(list_bingobingo)
    features, labels, newest_feature = hangod_predict.prepare_hangod_features_labels(df)
    x_train, x_test, y_train, y_test = hangod_predict.prepare_train_test_data(features, labels)
    clf = hangod_predict.get_trained_clf(x_train, y_train)
    pred = clf.predict(x_test)
    print('score:', clf.score(x_test, y_test))
    cm = confusion_matrix(pred, y_test)
    print(cm)
    print(int(newest_feature['identity']) + 1, ':', clf.predict(newest_feature))
    # plot
    plt.imshow(cm, cmap=plt.cm.Blues)
    tick_marks = range(2)
    classes = ['False', 'True']
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.show()

def fetch_bingobingo_to_database():
    session = Session()
    session_for_query = Session()
    pg = PageGetter()
    recent_bingo_content = pg.get()
    pp = PageParser()
    list_bingobingo = pp.parse(recent_bingo_content)
    while list_bingobingo:
        added = [session.add(bingobingo) for bingobingo in list_bingobingo if session_for_query.query(BingoBingo).filter(BingoBingo.identity == bingobingo.identity).one_or_none() is None]
        if not added:
            break
        pg.go_previous()
        older_bingo_content = pg.get()
        list_bingobingo = pp.parse(older_bingo_content)
    session.commit()


if __name__ == '__main__':
    fetch_bingobingo_to_database()
    predict_hangod()
