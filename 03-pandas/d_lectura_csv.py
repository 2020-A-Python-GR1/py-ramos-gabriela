# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:10:24 2020

@author: gabyl
"""
import pandas as pd
import os

path= "C://Users//gabyl//OneDrive//Documentos//GitHub-Repos//phyton//py-ramos-gabriela//03-pandas//data//artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10
    )

Columnas = ["id", "artist","title","medium","year",
            "acquisitionYear","height", "width","units"]

df2 = pd.read_csv(
    path, 
    nrows=10,
    usecols = Columnas)



df3 = pd.read_csv(
    path, 
    nrows=10,
    usecols = Columnas,
    index_col = "id")

