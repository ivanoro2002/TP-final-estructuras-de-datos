class Mensaje:  # Sea crea el mensaje 
    def __init__(self, emisor, destinatarios, asunto, contenido):
        self.__emisor = emisor
        self.__destinatarios = destinatarios
        self.__asunto = asunto
        self.__contenido = contenido    
      
    @property
    def emisor(self):
        return self.__emisor
        
    @property
    def destinatarios(self):
        return self.__destinatarios
    
    @property
    def asunto(self):
        return self.__asunto
