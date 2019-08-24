#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import json
import googlemaps

class DataReader:
    def __init__(self):
        self._context = None
        self._fname = None

    @property
    def context(self) -> str:
        return self._context
    @context.setter
    def context(self,f1):
        self._context = f1

    @property
    def fname(self) -> str:
        return self._fname
    @context.setter
    def fname(self, f2):
        self._fname = f2

    def new_file(self) -> str:
        return self._context+self._fname

    def csv_to_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file,encoding='utf-8', thousands=',',)

    def xls_to_dframe(self, header, usecols) -> object:
        file = self.new_file()
        return pd.read_excel(file, encoding='utf-8',header=header,usecols=usecols)

    def json_to_dframe(self) -> object:
        file = self.new_file()
        return json.load(open(file, encoding='utf-8'))

    def create_gmaps(self):
        return googlemaps.Client(key='')
