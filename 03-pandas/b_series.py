# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:56 2020

@author: gabyl
"""


import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))


series_a=pd.series(
   lista_numeros 
   )
series_b=pd.series(
    tupla_numeros)

series_c=pd.series(
    np_numeros)