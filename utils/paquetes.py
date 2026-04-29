import random
from datetime import datetime, timedelta

class Paquete:
    def __init__(self, idPaquete, remitente, destinatario, fechaEnvio, estado, peso, observaciones, ruta):
        self.idPaquete = idPaquete
        self.remitente = remitente
        self.destinatario = destinatario
        self.fechaEnvio = fechaEnvio
        self.estado = estado
        self.peso = peso
        self.observaciones = observaciones
        self.ruta = ruta

    def to_dict(self):
        return {
            "idPaquete": self.idPaquete,
            "remitente": self.remitente,
            "destinatario": self.destinatario,
            "fechaEnvio": self.fechaEnvio,
            "estado": self.estado,
            "peso": self.peso,
            "observaciones": self.observaciones,
            "ruta": self.ruta
        }


class GeneradorPaquetes:

    def __init__(self):
        self.personas = ['Carlos', 'Maria', 'Juan', 'Ana', 'Pedro', 'Luisa', 'Jose', 'Sofia', 'Diego', 'Laura']
        self.estados = ['En bodega', 'En tránsito', 'Entregado', 'Retrasado']
        self.observaciones = ['Frágil', 'Mantener seco', 'Entrega urgente', 'Requiere firma']
        self.rutas = ['Ruta A', 'Ruta B', 'Ruta C', 'Ruta D']

    def generar_paquete(self, idPaquete):
        return Paquete(
            idPaquete=idPaquete,
            remitente=random.choice(self.personas),
            destinatario=random.choice(self.personas),
            fechaEnvio=(datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
            estado=random.choice(self.estados),
            peso=round(random.uniform(0.5, 20), 2),  # en kg
            observaciones=random.choice(self.observaciones),
            ruta=random.choice(self.rutas)
        )

    def generar_paquetes(self, n):
        lista = []
        for i in range(1, n + 1):
            paquete = self.generar_paquete(i)
            lista.append(paquete.to_dict())
        return lista