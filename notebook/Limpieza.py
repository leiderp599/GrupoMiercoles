import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # Procesando los textos del DF sucio

    # 1. Limpiando los textos para eliminar espacios y mayúsculas
    data_frame_limpio["estado"] = data_frame_sucio["estado"].astype("string").str.strip().str.lower()
    data_frame_limpio["observaciones"] = data_frame_sucio["observaciones"].astype("string").str.strip().str.lower()
    data_frame_limpio["idRuta"] = data_frame_sucio["idRuta"].astype("string").str.strip().str.lower()

    # 2. Limpiando los textos para controlar valores inesperados
    valores_esperados_estado = ["pendiente", "en proceso", "completada", "cancelada"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
    data_frame_limpio["estado"].isin(valores_esperados_estado),
    pd.NA
    )
    valores_esperados_idRuta = ["ruta a", "ruta b", "ruta c", "ruta d"]
    data_frame_limpio["idRuta"] = data_frame_limpio["idRuta"].where(
    data_frame_limpio["idRuta"].isin(valores_esperados_idRuta),
    pd.NA
    )

    # Limpieza de datos numéricos
    # 1. Verificar que los números sí sean números
    data_frame_limpio["idOrden"] = pd.to_numeric(data_frame_limpio["idOrden"], errors='coerce')
    data_frame_limpio["preciototal"] = pd.to_numeric(data_frame_limpio["preciototal"], errors='coerce')

    # 2. Verifiquemos los valores numéricos esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["idOrden"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["preciototal"] >= 6.0]  # Basado en el rango de generación

    # Limpieza de FECHAS
    # 1. Verificar que el campo sí es una fecha
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors='coerce')

    # 2. Reemplazar fechas que no llegan por una fecha por defecto
    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_default)

    # 3. Novedades de datos vacíos
    columnas_obligatorias = ["idOrden", "estado", "preciototal", "idRuta"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio