import pandas as pd
import numpy as np
from seoul_crime.data_reader import DataReader
'''
cctv_columns(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
pop_columns(['자치구', '계', '계.1', '계.2', '65세이상고령자'], dtype='object')
'''
class CCTVModel:
    def __init__(self):
        self.dr = DataReader()
    def hook_process(self):
        print('-'*12,'1. CCTV 파일로 DF 생성','-'*12)
        self.get_cctv()

    def get_cctv(self):
        self.dr.context = './data/'
        self.dr.fname = 'cctv_in_seoul.csv'
        cctv = self.dr.csv_to_dframe()
        print('dr의 type은 ->',type(self.dr))
        print('cctv_columns ->',cctv.columns)
        self.dr.fname='pop_in_seoul.xls'
        pop = self.dr.xls_to_dframe(2,'B,D,G,J,N')
        print('pop_columns ->',pop.columns)
