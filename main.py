import pandas as pd
from utils.Orden import generar_ordenes
from notebook.Generador import crear_json, crear_csv
from notebook.Limpieza import limpiar_datos
from utils.generador_usuario import generar_usuarios

simulacion = generar_ordenes(100)
simulacion_ordenada = pd.DataFrame(simulacion)

# Aplicar limpieza de datos
simulacion_limpia = limpiar_datos(simulacion_ordenada)

crear_json(simulacion_limpia, "data/simulacion.json")
crear_csv(simulacion_limpia, "data/simulacion.csv")

#generar y guardas ordenes
ordenes = generar_ordenes(10)
ordenes_df = pd.DataFrame(ordenes)
print("Órdenes generadas:")
print(ordenes_df)
crear_json(ordenes_df, "data/ordenes.json")
crear_csv(ordenes_df, "data/ordenes.csv")

# Generar y guardar usuarios
usuarios = generar_usuarios(10)
usuarios_df = pd.DataFrame(usuarios)
print("Usuarios generados:")
print(usuarios_df)
crear_json(usuarios_df, "data/usuarios.json")
crear_csv(usuarios_df, "data/usuarios.csv")

print(simulacion_limpia)