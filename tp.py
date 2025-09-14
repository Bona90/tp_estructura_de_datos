from abc import ABC, abstractmethod

#  Interfaz para enviar mensajes.
class IEnviarMensaje(ABC):
    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto, cuerpo):
        pass

#  Interfaz para recibir mensajes.
class IRecibirMensajes(ABC):
    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass

#  Interfaz para listar mensajes.
class IListarMensajes(ABC):
    @abstractmethod
    def listar_mensajes(self):
        pass

class Usuario(IEnviarMensaje, IRecibirMensajes):
    def __init__(self, nombre, email, password):
        self.__nombre = nombre      #  usamos encapsulamiento para proteger los datos.
        self.__email = email
        self.__password = password
        self.__carpetas = []

# Getters y Setters
    def get_nombre(self):       #  usamos getters y setters en los atributos que consideramos necesarios.
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_email(self):
        return self.__email
    
    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    def set_password(self, nuevo_password):
        self.__password = nuevo_password
    
    def get_carpetas(self):
        return self.__carpetas
    
#Metodos de Usuario
    def enviar_mensaje(self, destinatario, asunto, cuerpo):
        pass
    def recibir_mensaje(self, mensaje):
        pass
    def listar_mensajes(self, carpeta):
        pass
    def mover_mensaje(self, mensaje, carpeta1, carpeta2):
        pass


# Clase Mensaje
class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo

    # Getters y Setters
    def get_remitente(self):
        return self.__remitente

    def get_destinatario(self):
        return self.__destinatario

    def set_destinatario(self, destinatario):
        self.__destinatario = destinatario

    def get_asunto(self):
        return self.__asunto

    def set_asunto(self, asunto):
        self.__asunto = asunto

    def get_cuerpo(self):
        return self.__cuerpo

# Métodos de Mensaje.
    def __str__(mensaje):
        pass

# Clase Carpeta
class Carpeta(IListarMensajes):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []  # lista de objetos Mensaje

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_mensajes(self):
        return self.__mensajes

#Métodos de clase Carpeta.
    def agregar_mensaje(self, mensaje):
        pass

    def eliminar_mensaje(self, mensaje):
        pass

    def listar_mensajes(self, carpeta):
        pass

# Clase ServidorCorreo
class ServidorCorreo(IEnviarMensaje, IRecibirMensajes):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__usuarios = []  # lista de objetos Usuario

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_usuarios(self):
        return self.__usuarios

#  Métodos de la clase Servidor Correo
    def registrar_usuario(self, usuario):
        pass

    def login(self, email, password):
        pass

    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        pass

    def recibir_mensaje(self, mensaje, destinatario):
        pass

