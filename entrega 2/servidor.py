class ServidorCorreo:  # Representa el servidor de mensajeria
    def __init__(self, email):  # Construye la estructura.
        self._email = email  # Registra el email del usuario.
        self._usuarios = []  # Lista de usuarios en la que se guardaran los mismos.

    def agregar_usuario(self, usuario):  # Agrega usuarios al servidor.
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario)  # Elimina usuarios del servidor.

    def obtener_usuarios(self):
        return self._usuarios  # Devuelve la lista de usuarios total en el servidor.
