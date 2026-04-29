import random
from datetime import datetime, timedelta

class Orden:
    def __init__(self, idOrden, idUsuario, fecha, estado, preciototal, observaciones, idRuta):
        self.idOrden = idOrden
        self.idUsuario = idUsuario
        self.fecha = fecha
        self.estado = estado
        self.preciototal = preciototal
        self.observaciones = observaciones
        self.idRuta = idRuta

    def to_dict(self):
        return {
            "idOrden": self.idOrden,
            "idUsuario": self.idUsuario,
            "fecha": self.fecha,
            "estado": self.estado,
            "preciototal": self.preciototal,
            "observaciones": self.observaciones,
            "idRuta": self.idRuta
        }


class GeneradorOrdenes:

    def __init__(self):
        self.usuarios = ['Carlos', 'Maria', 'Juan', 'Ana', 'Pedro', 'Luisa', 'Jose', 'Sofia', 'Diego', 'Laura']
        self.estados = ['Pendiente', 'En Proceso', 'Completada', 'Cancelada']
        self.observaciones = ['Entrega rápida', 'Requiere firma', 'Dejar en la puerta', 'Llamar al llegar']
        self.rutas = ['Ruta A', 'Ruta B', 'Ruta C', 'Ruta D']

    def generar_orden(self, idOrden):
        return Orden(
            idOrden=idOrden,
            idUsuario=random.choice(self.usuarios),
            fecha=(datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
            estado=random.choice(self.estados),
            preciototal=round(random.uniform(6000, 50000), 2),
            observaciones=random.choice(self.observaciones),
            idRuta=random.choice(self.rutas)
        )

    def generar_ordenes(self, n):
        lista = []
        for i in range(1, n + 1):
            orden = self.generar_orden(i)  # ID único automático
            lista.append(orden.to_dict())
        return lista