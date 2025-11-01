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
        self._carpetas["enviados"].agg_msjs(mensaje)  # A la carpeta "enviados", se le agrega el mensaje
        for user in self._servidor.obtener_usuarios():  # A cada usuario en el servidor 
            if user.email in destinatarios:  # Si el email del user es parte de los destinatarios
                user.recibir_msjs(mensaje)     # Este recibe el msj
                
    def recibir_msjs(self, mensaje): 
        if not isinstance(mensaje, Mensaje): # Valida que sea instancia de Mensaje. 
            raise TypeError("Esto no es un mensaje.") 
        dest = "inbox"  # Inicialmente los mensajes son recibidos en la carpeta "inbox" 
        for p, c_dest in self._filtros.items():   # Toma la posiciones de palabra clave y carpeta en el dic de filtros
            if p.lower() in mensaje.asunto.lower() or p.lower() in mensaje.emisor.lower():  # si el mensaje se encuentra contenida en "asunto" o "emisor"
                dest = c_dest     # Lo asigna al filtro que corresponda
                break     # Termina al eonctrar el primer filtro a aplicarse
        self.__carpetas[dest].agg_msjs(mensaje) # Agg el mensaje a la carpeta que corresponda

    def listar_msjs(self, carpeta):
        if carpeta in self._carpetas:   # Si el usuario quiere una carpeta y existe
            return self._carpetas[carpeta].listar_msjs()   # Lista los mensajes de la carpeta seleccionada
        return [] # Si no, no retorna nada.

    def agg_palabras(self, p_clave, c_dest):  # Solicita palabra a filtrar y carpeta destino para la misma.
        if c_dest not in self.__carpetas:   # Si la carpeta destino no está en las claves de carpetas.
            raise ValueError("La carpeta", c_dest, "no existe.") 
        self._filtros[p_clave.lower()] = c_dest # Si está, se agrega la palabra a la carpeta destino. (en minuscula)

    def pr_filtros(self):
        if not self._filtros:    # Si el usuario no agregò filtros
            return "No hay filtros existentes."
        else: 
            for p, c in self._filtros.items():     # Recorre con dos variables y toma ambas con .items 
                print(p, ":", c)         # Imprime palabra clave y carpeta


    def elim_filtro(self, p_clave):
        if p_clave in self._filtros:
            del self._filtros[p_clave.lower()]
        else:
            print("El filtro de la palabra ingresada es inexistente.")

