import pandas as pd
from utils.Orden import generar_ordenes
from notebook.Generador import crear_json, crear_csv
from notebook.Limpieza import limpiar_datos

simulacion = generar_ordenes(100)
simulacion_ordenada = pd.DataFrame(simulacion)

# Aplicar limpieza de datos
simulacion_limpia = limpiar_datos(simulacion_ordenada)

crear_json(simulacion_limpia, "data/simulacion.json")
crear_csv(simulacion_limpia, "data/simulacion.csv")