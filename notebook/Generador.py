import pandas as pd

def crear_json(dataframe, nombre_archivo):
    dataframe.to_json(nombre_archivo, orient='records', indent=4)

def crear_csv(dataframe, nombre_archivo):
    dataframe.to_csv(nombre_archivo, index=False)