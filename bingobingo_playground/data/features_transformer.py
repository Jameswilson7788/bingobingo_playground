#coding: utf-8
from sklearn.base import BaseEstimator, TransformerMixin


class FeaturesTransformer(BaseEstimator, TransformerMixin):
    """FeaturesTransformer

    transform features on bingobingo
    """

    def __init__(self, predict_number = 54):
        """

        :param predict_number: The number your want to predict
        """
        self.predict_number = predict_number

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        labels = X[['number{}'.format(self.predict_number)]][:-1]
        labels.columns = ['target']
        features = X.drop(0)
        return features.join(labels)



