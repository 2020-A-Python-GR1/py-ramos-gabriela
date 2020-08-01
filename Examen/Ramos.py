# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:11:29 2020

@author: gabyl
"""


import numpy as np     
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_1 = np.series(mylist)
serie2= np.series(myarr)