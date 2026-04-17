import pandas as pd
from utils.Orden import generar_ordenes

from notebook.Generador import crear_json, crear_csv

simulacion = generar_ordenes(100)
simulacion_ordenada=pd.DataFrame(simulacion)

crear_json(simulacion_ordenada, "data/simulacion.json")
crear_csv(simulacion_ordenada, "data/simulacion.csv")