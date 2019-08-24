#-*- coding:utf-8 -*-
from seoul_crime.cctv_pop import CCTVModel
from seoul_crime.crime_police import CrimeModel
from seoul_crime.foliumtest import FoliumTest
from seoul_crime.police_nml import PoliceNmlModel
class Controller:
    def __init__(self):
        self._cctv = CCTVModel()
        self._crime =CrimeModel()
        self._usa =FoliumTest()
        self._police = PoliceNmlModel()

    def execute(self):
        # cctv = self._cctv
        # cctv.hook_process()

        # crime = self._crime
        # crime.hook_process()

        usa = self._usa
        usa.hook()

        # pn= self._police
        # pn.hook()