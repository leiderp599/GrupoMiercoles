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
def generar_ordenes(n):

    #Defino atributos base
    generar_ordenes = []
    idOrden = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    idUsuario = ['carlos', 'maria', 'juan', 'ana', 'pedro', 'luisa', 'jose', 'sofia', 'diego', 'laura'] 
    estados = ['Pendiente', 'En Proceso', 'Completada', 'Cancelada']
    observaciones = ['Entrega rápida', 'Requiere firma', 'Dejar en la puerta', 'Llamar al llegar']
    idRuta = ['Ruta A', 'Ruta B', 'Ruta C', 'Ruta D']

    for i in range(1, n + 1):
        idOrden = random.choice(idOrden)
        idUsuario = random.choice(idUsuario)
        fecha = datetime.now() - timedelta(days=random.randint(0, 30))
        estado = random.choice(estados)
        preciototal = round(random.uniform(6.000, 50.000), 3)
        observacion = random.choice(observaciones)
        idRuta = random.choice(idRuta)

        orden = {
            'idOrden': idOrden,
            'idUsuario': idUsuario,
            'fecha': fecha.strftime('%Y-%m-%d'),
            'estado': estado,
            'preciototal': preciototal,
            'observaciones': observacion,
            'idRuta': idRuta
        }
        generar_ordenes.append(orden)
    return generar_ordenes