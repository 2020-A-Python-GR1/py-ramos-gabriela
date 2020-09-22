# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:25:38 2020

@author: gabyl
"""
import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "C:/GitHub-Gaby//py-ramos-gabriela//Proyecto II bimestre//csv//data//results.csv"
# artwork_data.pickle

df = pd.read_csv(path_guardado)

sub_df = df.iloc[:50519,:].copy()