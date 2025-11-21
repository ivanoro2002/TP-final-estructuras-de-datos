class Mensaje:  # Sea crea el mensaje 
    def __init__(self, emisor, destinatarios, asunto, contenido,prioridad = 0):
        self.__emisor = emisor
        self.__destinatarios = destinatarios
        self.__asunto = asunto
        self.__contenido = contenido    
        self._prioridad = prioridad
        self._leido = False
    @property
    def emisor(self):
        return self.__emisor
        
    @property
    def destinatarios(self):
        return self.__destinatarios
    
    @property
    def asunto(self):
        return self.__asunto

    @property
    def prioridad(self):
        return self._prioridad

    def marcar_urgente(self, level=1):
        self._prioridad = level