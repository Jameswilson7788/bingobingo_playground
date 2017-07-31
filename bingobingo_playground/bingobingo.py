# coding: utf-8
import json
from sqlalchemy import create_engine
from sqlalchemy import Column, String, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from collections import OrderedDict

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class BingoBingo(Base):
    """Represent a bingo bingo row

    """
    __tablename__ = 'bingobingos'
    identity = Column(String, primary_key=True)
    numbers = Column(PickleType)

    def __init__(self):
        self.identity = None
        self.numbers = OrderedDict.fromkeys(range(1, 81), False)

    def __repr__(self):
        return "<BingoBingo(identity={}, numbers={})>".format(self.identity, self.numbers)

Base.metadata.create_all(engine)
