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
        if not isinstance(mensaje, Mensaje): # Valida que sea instancia de Mensaje. 
            raise TypeError("Esto no es un mensaje.") 
        dest = "inbox"  # Inicialmente los mensajes son recibidos en la carpeta "inbox" 
        if "URGENTE".lower() in mensaje.asunto.lower():  # Si asunto contiene "urgente"
            self._urgente.append(mensaje)      # Irá directo a la cola de urgentes
        for p, c_dest in self._filtros.items():   # Toma la posiciones de palabra clave y carpeta en el dic de filtros
            if p.lower() in mensaje.asunto.lower() or p.lower() in mensaje.emisor.lower():  # si el mensaje se encuentra contenida en "asunto" o "emisor"
                dest = c_dest     # Lo asigna al filtro que corresponda
                break     # Termina al eonctrar el primer filtro a aplicarse
        self.__carpetas[dest].agg_msjs(mensaje) # Agg el mensaje a la carpeta que corresponda
                


    def listar_msjs(self, carpeta):
        if not isinstance(carpeta, str):
            raise TypeError("La carpeta debe ser escrita con texto.")
        if carpeta in self._carpetas:   # Si el usuario quiere una carpeta y existe
            if self._urgente:          # Si no esta vacia 
                for msj in self._urgente:
                    print("URGENTE:", msj.asunto)   
            return self._carpetas[carpeta].listar_msjs()   # Lista los mensajes de la carpeta seleccionada
        return [] # Si no, no retorna nada.