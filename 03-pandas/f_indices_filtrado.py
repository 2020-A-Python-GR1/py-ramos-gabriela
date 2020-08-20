# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:31:17 2020

@author: gabyl
"""


# f_indices_filtrado.py


import pandas as pd

path_guardado = "C://Users//gabyl//OneDrive//Documentos//GitHub-Repos//phyton//py-ramos-gabriela//03-pandas//data//artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) # Numpy Array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William' # Serie

print(blake.value_counts())

df_blake = df[blake] # DataFrame