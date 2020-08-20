# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:05:16 2020

@author: gabyl
"""


# d_lectura_csv.py

# 03_pandas
#   d_lectura_csv.py
#   data
#      artworw.csv

import pandas as pd
import os
    
path = "C://Users//gabyl//OneDrive//Documentos//GitHub-Repos//phyton//py-ramos-gabriela//03-pandas//data//artwork_data.csv"

# "C:\Users\gabyl\OneDrive\Documentos\GitHub-Repos\phyton\py-ramos-gabriela\03-pandas\dataartwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10)
columnas = ['id', 'artist', 'title',
            'medium', 'year',
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')

path_guardado = "C://Users//gabyl//OneDrive//Documentos//GitHub-Repos//phyton//py-ramos-gabriela//03-pandas//data//artwork_data.pickle"
# artwork_data.pickle

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)
