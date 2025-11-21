from servidor import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje
from grafo import GrafoServidores

# Creamos el grafo de servidores
red = GrafoServidores()

def menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1) Crear servidor")
    print("2) Crear usuario en servidor")
    print("3) Conectar servidores")
    print("4) Enviar mensaje entre servidores (BFS/DFS)")
    print("0) Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del servidor: ")
        servidor = ServidorCorreo(nombre)
        red.agregar_servidor(servidor)
        print("Servidor agregado a la red.")

    elif opcion == "2":
        nombre_servidor = input("Servidor donde agregar el usuario: ")
        servidor = red._GrafoServidores__servidores.get(nombre_servidor)

        if servidor:
            nombre = input("Nombre del usuario: ")
            mail = input("Email: ")
            usuario = Usuario(nombre, mail, servidor, None)
            servidor.agregar_usuario(usuario)
            print("Usuario creado.")
        else:
            print("Servidor no encontrado.")

    elif opcion == "3":
        s1 = input("Servidor origen: ")
        s2 = input("Servidor destino: ")
        try:
            red.conectar_servidores(s1, s2)
            print("Servidores conectados.")
        except ValueError as e:
            print(e)

    elif opcion == "4":
        origen = input("Servidor origen: ")
        destino = input("Servidor destino: ")
        metodo = input("Método (bfs o dfs): ").lower()

        asunto = input("Asunto: ")
        contenido = input("Contenido: ")
        emisor = input("Email emisor: ")
        destinatario = input("Email destinatario: ")

        mensaje = Mensaje(emisor, [destinatario], asunto, contenido)

        ruta = red.enviar_por_red(origen, destino, mensaje, metodo)

        if ruta:
            print("Mensaje enviado. Ruta utilizada:", ruta)
        else:
            print("No existe ruta entre los servidores.")

    elif opcion == "0":
        break

    else:
        print("Opción inválida.")
