# Clase Carpeta: contiene subcarpetas y mensajes de un usuario.
class Carpeta(IListarMensajes):
    def __init__(self, nombre, padre=None):
        self.__nombre = nombre
        self.__mensajes = []
        self.__subcarpetas = []    # lista de objetos Carpeta (estructura recursiva)
        self.__padre = padre       # referencia a la carpeta padre (None si es raíz)

    # ---------------- Getters y Setters ----------------
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_mensajes(self):
        return self.__mensajes

    def get_subcarpetas(self):
        return self.__subcarpetas

    def get_padre(self):
        return self.__padre

    # ---------------- Gestión de mensajes ----------------
    def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)

    def listar_mensajes(self):
        return [str(m) for m in self.__mensajes]

    # ---------------- Gestión de carpetas ----------------
    def agregar_subcarpeta(self, subcarpeta):
        """Agrega una subcarpeta al árbol."""
        subcarpeta.__padre = self
        self.__subcarpetas.append(subcarpeta)

    def buscar_subcarpeta(self, nombre):
        """Busca recursivamente una subcarpeta por nombre."""
        for sub in self.__subcarpetas:
            if sub.get_nombre() == nombre:
                return sub
            encontrada = sub.buscar_subcarpeta(nombre)
            if encontrada:
                return encontrada
        return None

    def listar_carpetas(self, nivel=0):
        """Devuelve un listado jerárquico de carpetas y subcarpetas."""
        estructura = "  " * nivel + f"[{self.__nombre}]\n"
        for sub in self.__subcarpetas:
            estructura += sub.listar_carpetas(nivel + 1)
        return estructura

    # ---------------- Funcionalidades extra ----------------
    def mover_mensaje(self, mensaje, carpeta_destino):
        """
        Mueve un mensaje de la carpeta actual a otra carpeta destino.
        """
        if mensaje in self.__mensajes:
            self.eliminar_mensaje(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)

    def buscar_mensajes_por_asunto(self, texto):
        """
        Busca recursivamente todos los mensajes que contengan 'texto' en el asunto.
        """
        encontrados = []
        for m in self.__mensajes:
            if texto.lower() in m.get_asunto().lower():
                encontrados.append(m)
        for sub in self.__subcarpetas:
            encontrados.extend(sub.buscar_mensajes_por_asunto(texto))
        return encontrados

    def buscar_mensajes_por_remitente(self, remitente):
        """
        Busca recursivamente todos los mensajes enviados por un remitente específico.
        """
        encontrados = []
        for m in self.__mensajes:
            if m.get_remitente().lower() == remitente.lower():
                encontrados.append(m)
        for sub in self.__subcarpetas:
            encontrados.extend(sub.buscar_mensajes_por_remitente(remitente))
        return encontrados
