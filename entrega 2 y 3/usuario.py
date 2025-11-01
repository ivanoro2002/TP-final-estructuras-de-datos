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
        self._mail = email
        self._servidor = servidor
        self.__carpetas = {
            "inbox": Carpeta("inbox"),
            "enviados": Carpeta("enviados"),
            "papelera": Carpeta("papelera")
        }    
        self._filtros = {}

    @property
    def email(self):
        return self._email
    
    @property
    def nombre(self):
        return self._nombre

    def enviar_msjs(self, destinatarios, asunto, contenido):
        if not isinstance(asunto, str) or not isinstance(contenido, str): # Valida si el contenido de las claves sea del tipo correspondiente.
            raise TypeError("El asunto y el contenido debe ser texto (strings).")
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
