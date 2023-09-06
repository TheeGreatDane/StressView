import lasio
import pandas as pd
import os

filename = open("TestFile.las")
las = lasio.read(filename)
# Show data 
# print(las.curves)
# Make LAS file into DataFrame
dflas = las.df().reset_index()
# print(dflas)

# Clean df, remove depths with incomplete data
dflas_clean = dflas.dropna().copy()
# print(dflas_clean)
dflas_clean.to_csv("TestFile.csv")
