
class GrafoServidores:
    def __init__(self):
        # Diccionario donde la clave es el nombre del servidor
        # y el valor es la lista de servidores conectados.
        self.__conexiones = {}
        # Diccionario para guardar los servidores reales (instancias)
        self.__servidores = {}

    def agregar_servidor(self, servidor):
        """
        Agrega un servidor al grafo.
        El servidor debe ser una instancia de ServidorCorreo.
        """
        nombre = servidor._ServidorCorreo__email if hasattr(servidor, "_ServidorCorreo__email") else servidor._nombre

        # Guardamos la instancia
        self.__servidores[nombre] = servidor

        # Inicializamos su lista de conexiones
        if nombre not in self.__conexiones:
            self.__conexiones[nombre] = []

    def conectar_servidores(self, servidor1, servidor2):
        """
        Conecta dos servidores en ambas direcciones.
        Cada servidor se relaciona con el otro.
        """
        if servidor1 not in self.__conexiones or servidor2 not in self.__conexiones:
            raise ValueError("Alguno de los servidores no existe en la red.")

        # Conexión bidireccional
        if servidor2 not in self.__conexiones[servidor1]:
            self.__conexiones[servidor1].append(servidor2)

        if servidor1 not in self.__conexiones[servidor2]:
            self.__conexiones[servidor2].append(servidor1)

    def bfs(self, origen, destino):
        """
        Busca un camino desde 'origen' hasta 'destino'
        usando BFS (amplitud).
        Devuelve la lista de servidores visitados en orden.
        """
        visitados = set()
        cola = deque([[origen]])

        while cola:
            camino = cola.popleft()
            actual = camino[-1]

            if actual == destino:
                return camino

            if actual not in visitados:
                visitados.add(actual)
                for vecino in self.__conexiones.get(actual, []):
                    cola.append(camino + [vecino])

        return None

    def dfs(self, origen, destino):
        """
        Busca un camino desde 'origen' hasta 'destino'
        usando DFS (profundidad).
        """
        pila = [[origen]]
        visitados = set()

        while pila:
            camino = pila.pop()
            actual = camino[-1]

            if actual == destino:
                return camino

            if actual not in visitados:
                visitados.add(actual)
                for vecino in self.__conexiones.get(actual, []):
                    pila.append(camino + [vecino])

        return None

    def enviar_por_red(self, origen, destino, mensaje, metodo="bfs"):
        """
        Simula el envío de un mensaje entre servidores.
        Elige BFS o DFS según parámetro.
        No modifica tu lógica de Usuario ni ServidorCorreo.
        """
        if metodo.lower() == "bfs":
            ruta = self.bfs(origen, destino)
        else:
            ruta = self.dfs(origen, destino)

        return ruta  # el recorrido real la hace el usuario.
