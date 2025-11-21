from mensaje import Mensaje


class Carpeta:  # Se crea la carpeta correspondiente.
    def __init__(self, nombre):
        self.__nombre = nombre  # Recibe el nombre de la carpeta (inbox, enviados, etc)
        self.__mensajes = []  # Crea la lista vacia de mensajes
        self.__subcarpetas = []  # lista de subcarpetas

# ---------------------------#    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def mensajes(self):
        return self.__mensajes  
    
    @property
    def subcarpetas(self):
        return self.__subcarpetas
# -------------------------#

    def agg_msjs(self, mensaje):  # Se define la función y recibe el mensaje
        return self.__mensajes.append(mensaje)  # Agrega el mensaje a la lista de mensajes
    
    def delete_msjs(self, mensaje):  # Se define la función y se recibe el parametro del mensaje
        if mensaje in self.__mensajes:  # Busqueda de msj en la lista de msjs
            self.__mensajes.remove(mensaje)  # Elimina msj de una lista
    
    def listar_msjs(self):
        return self.__mensajes  # Recibe todos los mensajes.

    def agg_subcarpeta(self, subcarpeta):
        self.__subcarpetas.append(subcarpeta) # Agg carpetas "hijas"
        
    def buscar_subcarpeta(self, nombre_c):
        if self.__nombre == nombre_c:       # Si el nombre de la carpeta coincide con la actualmente recorrida
            return self                 # retorna
        for i in self.__subcarpetas:       
            si = i.buscar_subcarpeta(nombre_c) # Busca en cada subcarpeta 
            if si:
                return si          
        return None # Si no encuentra, retorna None
    
    def buscar_msj(self, mensaje):
        if not isinstance(mensaje, str):  # Corregir a strings 
            msj = str(mensaje)
        msj = msj.lower()
        hallados = []
        for m in self.__mensajes:
            if mensaje.lower() in m.asunto.lower() or mensaje.lower() in m.emisor.lower(): # Busca dentro del contenido del asunto y del correo emisor.
                hallados.append(m) 
        for s in self.__subcarpetas: # Llamada recursiva a las subcarpetas
            hallados += s.buscar_msj(mensaje)  # Busqueda recursiva y listar al encontrar.
        return hallados # Retorna todos los listados

    def mover_msjs(self, mensaje, carpeta_destino): 
        if not isinstance(mensaje, Mensaje):
            raise TypeError("No ingresó un mensaje existente.")
        
        if not isinstance(carpeta_destino, Carpeta):
            raise TypeError("No ingresó una carpeta existente.")

        if mensaje in self.__mensajes:   # Cond.Base, aca empieza y puede terminar.
            self.__mensajes.remove(mensaje) # Si encuentra, lo elimina de la carpeta en la carpeta actual
            carpeta_destino.agg_msjs(mensaje) # Lo agrega a la carp indicada con el metodo agg.msjs
            return "Mensaje movido con èxito."
        for sub in self.__subcarpetas:        # Al no estar en la carpeta actual, empieza a recorrer las sub_c
            if sub.mover_msjs(mensaje, carpeta_destino):  # Implementa a cada sub carpeta la busqueda del msj de forma recursiva   
                return True
        return False # Msj no encontrado. 
    
