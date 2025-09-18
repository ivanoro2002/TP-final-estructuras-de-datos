from abc import ABC, abstractmethod

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

class ServidorCorreo:  #Representa el servidor de mensajeria
    def __init__(self, email): # Construye la estructura.
        self._email = email # Registra el email del usuario.
        self._usuarios = [] # Lista de usuarios en la que se guardaran los mismos.

    def agregar_usuario(self, usuario): # Agrega usuarios al servidor.
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario) # Elimina usuarios del servidor.

    def obtener_usuarios(self):
        return self._usuarios  # Devuelve la lista de usuarios total en el servidor.

class Usuario(GestionCorreo):
    def __init__(self, nombre,email, servidor,carpetas):
        self._nombre = nombre
        self._email = email
        self._servidor = servidor
        self._carpetas = {
            "inbox": Carpeta("inbox"),    # Asignación de nombre a 
            "enviados": Carpeta("enviados"),  # Cada Carpeta
            "papelera": Carpeta("papelera")
        }    

    def enviar_msjs(self, destinatarios, asunto, contenido):
        mensaje = Mensaje(self._email, destinatarios, asunto, contenido)
        self._carpetas["enviados"].agg_msjs(mensaje)

    def recibir_msjs(self, mensaje):
        self._carpetas["inbox"].agg_msjs(mensaje)

    def listar_msjs(self, carpeta):
        if carpeta in self._carpetas:
            return self._carpetas[carpeta].listar_msjs()
        return []
    
class Mensaje: # Sea crea el mensaje 
    def __init__(self, emisor, destinatarios, asunto, contenido):
        self._emisor = emisor
        self._destinatarios = destinatarios
        self._asunto = asunto
        self._contenido = contenido    
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def emisor(self):
        return self._emisor
        
    @property
    def destinarios(self):
        return self._destinarios
    
    @property
    def asunto(self):
        return self._asuntos
    
class Carpeta: # Se crea la carpeta correspondiente.
    def __init__(self, nombre):
        self.nombre = nombre # Recibe el nombre de la carpeta (inbox, enviados, etc)
        self.mensajes = [] # Crea la lista vacia de mensajes
    
    def msjes(self):
        return self._mensajes # Retorna todos los mensajes
    
    def agg_msjs(self, mensaje): # Se define la función y recibe el mensaje
        return self._mensajes.append(mensaje) # Agrega el mensaje a la lista de mensajes
    
    def delete_msjs(self, mensaje): # Se define la función y se recibe el parametro del mensaje
        if mensaje in self._mensajes: # Busqueda de msj en la lista de msjs
            self._mensajes.remove(mensaje)  # Elimina msj de una lista
    
    def listar_msjs(self):
        return self._mensajes # Recibe todos los mensajes.

