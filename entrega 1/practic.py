class Usuario:
    def __init__(self, nombre, email, servidor):
        self.__nombre = nombre
        self.__email = email
        self.__servidor = servidor
        self.__carpetas = {
            "inbox": Carpeta("inbox"),
            "enviados": Carpeta("enviados"),
            "papelera": Carpeta("papelera")
        }


    def recibir_mensaje(self, mensaje):
        self.__carpetas["inbox"].agregar_mensaje(mensaje)

    def enviar_mensaje(self, destinatario, asunto, contenido, fecha):
        mensaje = Mensaje(self.__email, destinatario, asunto, contenido, fecha)
        self.__carpetas["enviados"].agregar_mensaje(mensaje)
        self.__servidor.enviar_mensaje(destinatario, mensaje)


class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido, fecha):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__contenido = contenido
        self.__fecha = fecha
        self.__leido = False

    # Métodos
    def marcar_como_leido(self):
        self.__leido = True

    def marcar_como_no_leido(self):
        self.__leido = False

    def mostrar(self):
        estado = "Leído" if self.__leido else "No leído"
        return (f"Asunto: {self.__asunto}\n"
                f"De: {self.__remitente}\n"
                f"Para: {self.__destinatario}\n"
                f"Fecha: {self.__fecha}\n"
                f"Estado: {estado}\n"
                f"Contenido:\n{self.__contenido}")


class Carpeta:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []

    def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)

    def listar_mensajes(self):
        return [m.mostrar() for m in self.__mensajes]


class ServidorCorreo:
    def __init__(self):
        self.__usuarios = []

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        if usuario in self.__usuarios:
            self.__usuarios.remove(usuario)


    def enviar_mensaje(self, destinatario_email, mensaje):
        for usuario in self.__usuarios:
            if usuario.email == destinatario_email:
                usuario.recibir_mensaje(mensaje)
                break

    def obtener_usuarios(self):
        return self.__usuarios
    
    
    
