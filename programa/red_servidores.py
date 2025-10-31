from collections import deque

class RedServidores:
    def __init__(self):
        self._conexiones = {}  #Usamos un diccionario donde la clave es: ServidorCorreo, y el valor: lista de ServidorCorreo

    def agregar_servidor(self, servidor):
        if servidor not in self._conexiones:
            self._conexiones[servidor] = []

    def conectar(self, servidor1, servidor2):
        # grafo no dirigido
        self.agregar_servidor(servidor1)
        self.agregar_servidor(servidor2)
        if servidor2 not in self._conexiones[servidor1]:
            self._conexiones[servidor1].append(servidor2)
        if servidor1 not in self._conexiones[servidor2]:
            self._conexiones[servidor2].append(servidor1)

    def bfs(self, origen, destino):#Devuelve la ruta entre origen y destino usando BFS.
        
        visitados = set()
        cola = deque([(origen, [origen])])

        while cola:
            actual, camino = cola.popleft()
            if actual == destino:
                return camino
            visitados.add(actual)
            for vecino in self._conexiones.get(actual, []):
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
        return None

    def dfs(self, origen, destino, visitados=None, camino=None):#Devuelve la ruta entre origen y destino usando DFS (recursivo).
        
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = [origen]

        if origen == destino:
            return camino

        visitados.add(origen)
        for vecino in self._conexiones.get(origen, []):
            if vecino not in visitados:
                resultado = self.dfs(vecino, destino, visitados, camino + [vecino])
                if resultado:
                    return resultado
        return None

    def enviar_mensaje(self, origen, destino, mensaje, metodo='bfs'):#Simula el envío del mensaje entre servidores, paso a paso.
        if metodo == 'bfs':
            ruta = self.bfs(origen, destino)
        else:
            ruta = self.dfs(origen, destino)

        if not ruta:
            print("No hay ruta disponible entre los servidores.")
            return

        # Simular paso del mensaje por cada servidor de la ruta
        for i in range(len(ruta) - 1):
            actual = ruta[i]
            siguiente = ruta[i + 1]
            print("Enviando mensaje desde", actual.get_nombre(), "a", siguiente.get_nombre(), "...")

        # Entregar el mensaje en el servidor destino
        servidor_destino = ruta[-1]
        usuario_destino = servidor_destino.get_usuario(mensaje.get_destinatario())
        servidor_destino.recibir_mensaje(mensaje, usuario_destino)
