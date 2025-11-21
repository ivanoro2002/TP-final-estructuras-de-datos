class ServidorCorreo:  # Representa el servidor de mensajeria
    def __init__(self, email):  # Construye la estructura.
        self.__email = email  # Registra el email del usuario.
        self.__usuarios = []  # Lista de usuarios en la que se guardaran los mismos.

    def agregar_usuario(self, usuario):  # Agrega usuarios al servidor.
        self.__usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self.__usuarios.remove(usuario)  # Elimina usuarios del servidor.

    def obtener_usuarios(self):
        return self.__usuarios  # Devuelve la lista de usuarios total en el servidor.
