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

class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido, fecha):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._contenido = contenido
        self._fecha = fecha
        self._leido = False

    def marcar_como_leido(self):
        self._leido = True
        
    def marcar_como_no_leido(self):
        self._leido = False

    
class Carpeta:
    def __init__(self,nombre):
        self._nombre = nombre
        self._mensajes = []

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def eliminar_mensajes(self,mensaje):
        self._mensajes.remove(mensaje)

    def listar_mensajes(self):
        return self._mensajes

class ServidorCorreo:
    def __init__(self, email):
        self._email = email
        self._usuarios = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario)

    def obtener_usuarios(self):
        return self._usuarios
