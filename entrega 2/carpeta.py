class Carpeta:  # Se crea la carpeta correspondiente.
    def __init__(self, nombre):
        self.nombre = nombre  # Recibe el nombre de la carpeta (inbox, enviados, etc)
        self._mensajes = []  # Crea la lista vacia de mensajes
    
    def msjes(self):
        return self._mensajes  # Retorna todos los mensajes
    
    def agg_msjs(self, mensaje):  # Se define la función y recibe el mensaje
        return self._mensajes.append(mensaje)  # Agrega el mensaje a la lista de mensajes
    
    def delete_msjs(self, mensaje):  # Se define la función y se recibe el parametro del mensaje
        if mensaje in self._mensajes:  # Busqueda de msj en la lista de msjs
            self._mensajes.remove(mensaje)  # Elimina msj de una lista
    
    def listar_msjs(self):
        return self._mensajes  # Recibe todos los mensajes.
