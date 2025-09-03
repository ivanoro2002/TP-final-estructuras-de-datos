# apartado de clases

class Usuario:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email
        

class Servidorcorreo:
    def __init__(self, dominio):
        self._dominio = dominio
        self._usuarios = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario)

    def obtener_usuarios(self):
        return self._usuarios
