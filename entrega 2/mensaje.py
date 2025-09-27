class Mensaje:  # Sea crea el mensaje 
    def __init__(self, emisor, destinatarios, asunto, contenido):
        self._emisor = emisor
        self._destinatarios = destinatarios
        self._asunto = asunto
        self._contenido = contenido    
      
    @property
    def emisor(self):
        return self._emisor
        
    @property
    def destinatarios(self):
        return self._destinarios
    
    @property
    def asunto(self):
        return self._asunto
