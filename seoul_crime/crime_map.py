from seoul_crime.data_reader import DataReader
import numpy as np
import pandas as pd
import folium

class CrimeMap:
    def __init__(self):
        self.dr = DataReader()

    def hook(self):
        print('-' * 12, '1, crime_map', '-' * 12)
        self.create_seoul_crime_map()

    def create_seoul_crime_map(self):
        self.dr.context = './saved_data/'
        self.dr.fname = 'police_norm.csv'
        pn = self.dr.csv_to_dframe()
        print(pn)

