from servidor import ServidorCorreo
from usuario import Usuario

if __name__ == "__main__":
    # Servidor
    servidor = ServidorCorreo("servidor@mail.com")

    # Usuarios
    usuario1 = Usuario("Juan", "juan@mail.com", servidor, {})
    usuario2 = Usuario("Ana", "ana@mail.com", servidor, {})

    # Agregar usuarios al servidor
    servidor.agregar_usuario(usuario1)
    servidor.agregar_usuario(usuario2)

    # Enviar mensaje
    usuario1.enviar_msjs(["ana@mail.com"], "Saludo", "Hola Ana, ¿cómo estás?")

    # Listar mensajes recibidos
    for msj in usuario2.listar_msjs("inbox"):
        print(f"De: {msj.emisor} | Asunto: {msj.asunto}")
