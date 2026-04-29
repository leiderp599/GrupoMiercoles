#Funcion para generar N servicios de ordenes

#idOrden(integer)
#idUsuario(integer)
#fecha(date)
#estado(string)
#preciototal(float)
#observaciones(string)
#idRuta(integer)

import random
from datetime import datetime, timedelta

def generar_nombre():
    nombres = ['Carlos', 'Maria', 'Juan', 'Ana', 'Pedro', 'Luisa', 'Jose', 'Sofia', 'Diego', 'Laura']
    return random.choice(nombres)

def generar_ordenes(n):

    #Defino atributos base
    generar_ordenes = []
    idOrden = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    idUsuario = ['carlos', 'maria', 'juan', 'ana', 'pedro', 'luisa', 'jose', 'sofia', 'diego', 'laura'] 
    estados = ['Pendiente', 'En Proceso', 'Completada', 'Cancelada']
    observaciones = ['Entrega rápida', 'Requiere firma', 'Dejar en la puerta', 'Llamar al llegar']
    idRuta = ['Ruta A', 'Ruta B', 'Ruta C', 'Ruta D']

    for i in range(1, n + 1):
        orden_id = random.choice(idOrden)
        usuario_id = random.choice(idUsuario)
        fecha = datetime.now() - timedelta(days=random.randint(0, 30))
        estado = random.choice(estados)
        preciototal = round(random.uniform(6.000, 50.000), 3)
        observacion = random.choice(observaciones)
        ruta_id = random.choice(idRuta)

        orden = {
            'idOrden': generar_nombre(),
            'idUsuario': generar_nombre(),
            'fecha': fecha.strftime('%Y-%m-%d'),
            'estado': generar_nombre(),
            'preciototal': preciototal,
            'observaciones': generar_nombre(),
            'idRuta': generar_nombre()
        }
        generar_ordenes.append(orden)
    return generar_ordenes