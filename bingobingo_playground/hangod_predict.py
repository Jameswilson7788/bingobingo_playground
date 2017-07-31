#coding: utf-8
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

def prepare_train_test_data(features, labels):
    x_train, x_test, y_train, y_test = train_test_split(features, labels)
    return x_train, x_test, y_train, y_test

def get_trained_clf(features, labels):
    clf = AdaBoostClassifier()
    clf.fit(features, labels)
    return clf

def prepare_hangod_features_labels(bingobingo_dataframe):
    features = bingobingo_dataframe.drop(0)
    labels = bingobingo_dataframe['number54'][:-1]
    newest_feature = bingobingo_dataframe[:1]
    return features, labels, newest_feature
