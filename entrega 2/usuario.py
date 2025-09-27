from abc import ABC, abstractmethod
from carpeta import Carpeta
from mensaje import Mensaje

class GestionCorreo(ABC):
    @abstractmethod
    def enviar_msjs(self, destinarios: str, asunto: str, contenido: str):
        pass

    @abstractmethod    
    def recibir_msjs(self, mensaje: str):
        pass

    @abstractmethod
    def listar_msjs(self, carpeta: str):
        pass


class Usuario(GestionCorreo):
    def __init__(self, nombre, email, servidor, carpetas):
        self._nombre = nombre
        self._email = email
        self._servidor = servidor
        self._carpetas = {
            "inbox": Carpeta("inbox"),
            "enviados": Carpeta("enviados"),
            "papelera": Carpeta("papelera")
        }    

    def enviar_msjs(self, destinatarios, asunto, contenido):
        mensaje = Mensaje(self._email, destinatarios, asunto, contenido)
        self._carpetas["enviados"].agg_msjs(mensaje)
        for user in self._servidor.obtener_usuarios():
            if user._email in destinatarios:
                user.recibir_msjs(mensaje)
                
    def recibir_msjs(self, mensaje):
        self._carpetas["inbox"].agg_msjs(mensaje)

    def listar_msjs(self, carpeta):
        if carpeta in self._carpetas:
            return self._carpetas[carpeta].listar_msjs()
        return []
