# apartado de clases

class Usuario:
    def __init__(self, nombre,email, servidor,carpetas):
        self._nombre = nombre
        self._email = email
        self._servidor = servidor
        self._carpetas = carpetas # diccionario de carpetas
        self._carpetas = {
            "inbox": carpetas("inbox"),
            "enviados": carpetas("enviados"),
            "papelera": carpetas("papelera")
        }


class Servidorcorreo:
    def __init__(self, email):
        self._email = email
        self._usuarios = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario)

    def obtener_usuarios(self):
        return self._usuarios
