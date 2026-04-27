import random
from datetime import datetime, timedelta

def generar_usuarios(numeroUsuarios):

    nombres = ["carlos", "maria", "juan", "ana"]
    correos = ["gmail.com", "hotmail.com", "yahoo.com"]
    roles = ["admin", "cliente", "empleado"]
    estados = ["activo", "inactivo"]

    fechaInicio = datetime(2026, 1, 2)

    usuarios = []
    for _ in range(numeroUsuarios):

        usuario = {
            "idUsuario": random.randint(0, 200),
            "nombre": random.choice(nombres),
            "correo": random.choice(nombres) + str(random.randint(1,100)) + "@" + random.choice(correos),
            "contraseña": "pass" + str(random.randint(1000,9999)),
            "rol": random.choice(roles),
            "estado": random.choice(estados),
            "fechaRegistro": fechaInicio + timedelta(days=random.randint(0, 60))
        }

        probabilidadError = random.random()

        if(probabilidadError < 0.2):
            usuario["idUsuario"] = None
        elif(probabilidadError < 0.4):
            usuario["nombre"] = random.choice(["12345", "???"])
        elif(probabilidadError < 0.5):
            usuario["correo"] = "correo_mal"
        elif(probabilidadError < 0.8):
            usuario["rol"] = " " + usuario["rol"].upper()
        elif(probabilidadError < 0.9):
            usuario["fechaRegistro"] = None

        usuarios.append(usuario)

    return usuarios