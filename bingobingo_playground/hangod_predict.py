#coding: utf-8
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from bingobingo_playground.data import prepare_feature_labels

def prepare_train_test_data(features, labels):
    x_train, x_test, y_train, y_test = train_test_split(features, labels)
    return x_train, x_test, y_train, y_test

def get_trained_clf(features, labels):
    clf = GaussianNB()
    clf.fit(features, labels)
    return clf

def prepare_hangod_features_labels(bingobingo_dataframe):
    features, labels = prepare_feature_labels(bingobingo_dataframe, 54)
    newest_feature = bingobingo_dataframe[:1]
    return features, labels, newest_feature
