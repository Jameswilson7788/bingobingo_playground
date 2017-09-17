#coding: utf-8
from sklearn.naive_bayes import GaussianNB
from bingobingo_playground.data import prepare_feature_labels

def get_trained_clf(features, labels):
    clf = GaussianNB()
    clf.fit(features, labels)
    return clf

def prepare_hangod_features_labels(bingobingo_dataframe):
    features, labels = prepare_feature_labels(bingobingo_dataframe, 54)
    newest_feature = bingobingo_dataframe[:1]
    return features, labels, newest_feature
