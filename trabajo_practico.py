from abc import ABC, abstractmethod

#  Interfaz IEnviarMensaje: define la capacidad de una clase para enviar mensaje.
class IEnviarMensaje(ABC):
    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto, cuerpo):
        pass

#  Interfaz IRecibirMensajes: define la capacidad para recibir mensajes.
class IRecibirMensajes(ABC):
    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass

#  Interfaz IListarMensajes: define la capacidad de una carpeta de listar mensajes.
class IListarMensajes(ABC):
    @abstractmethod
    def listar_mensajes(self):
        pass

#  Clase Usuario: representa a un usuario del sistema de correo.
class Usuario(IEnviarMensaje, IRecibirMensajes):
    def __init__(self, nombre, email, password):
        self.__nombre = nombre
        self.__email = email
        self.__password = password
        self.__carpetas = [Carpeta("Bandeja de entrada")] #Cada usuario arranca con su carpeta "Bandeja de entrada" para que los mesajes se guarden ahi y no se pierdan.

    # Getters y Setters
    def get_nombre(self):
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
    
    # Métodos de Usuario
    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo): 
        mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)      # Crea un objeto Mensaje y lo devuelve con el return
        return mensaje

    def recibir_mensaje(self, mensaje):
        for carpeta in self.__carpetas:
            if carpeta.get_nombre().lower() == "bandeja de entrada":    #Ya sabemos que existe la carpeta Bandeja de entrada, y guardamos ahi el mensaje.
                carpeta.agregar_mensaje(mensaje)
                return

    def listar_mensajes(self, carpeta):
        return carpeta.listar_mensajes()    #Pide que devuelva los mensajes que contiene la carpeta.

    def mover_mensaje(self, mensaje, carpeta1, carpeta2):
        if mensaje in carpeta1.get_mensajes():  #Aca podemos mover mensajes entre carpetas, para por ejemplo mandar un mensaje a una carpeta "Spam"
            carpeta1.eliminar_mensaje(mensaje)
            carpeta2.agregar_mensaje(mensaje)


# Clase Mensaje: representa un mensaje de correo.
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

    # Métodos de Mensaje
    def __str__(self):      #Devuelve el mensaje en forma de texto
        return f"De: {self.__remitente} | Para: {self.__destinatario} | Asunto: {self.__asunto}\n{self.__cuerpo}"


# Clase Carpeta: contiene mensajes de un usuario.
class Carpeta(IListarMensajes):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_mensajes(self):
        return self.__mensajes

    # Métodos de clase Carpeta
    def agregar_mensaje(self, mensaje): #Agrega un mensaje a la lista de la carpeta
        self.__mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):    #Borra un mensaje de la carpeta (si está presente)
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)

    def listar_mensajes(self):
        return [str(m) for m in self.__mensajes]    #Devuelve los mensajes de la carpeta en formato texto.


# Clase ServidorCorreo: gestiona usuarios y permite el envío y recepción de mensajes.
class ServidorCorreo(IEnviarMensaje, IRecibirMensajes):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__usuarios = []

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_usuarios(self):
        return self.__usuarios

    # Métodos de la clase ServidorCorreo
    def registrar_usuario(self, usuario):   #Registra un usuario nuevo al servidor
        if self.buscar_usuario(usuario.get_email()) is None:
            self.__usuarios.append(usuario)
            return True
        return False

    def login(self, email, password):   #El login es basicamente una verificacion de un usuario con una contraseña
        usuario = self.buscar_usuario(email)
        if usuario and usuario._Usuario__password == password:
            return usuario
        return None

    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):  # Crea un mensaje y lo envía a "recibir_mensaje"
        mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
        self.recibir_mensaje(mensaje, destinatario)

    def recibir_mensaje(self, mensaje, destinatario):    # Busca un usuario registrado y le entrega el mensaje.
        usuario = self.buscar_usuario(destinatario)
        if usuario:
            usuario.recibir_mensaje(mensaje)

    def buscar_usuario(self, email):    #Busca un usuario por su email dentro de la lista de registrados
        for usuario in self.__usuarios:
            if usuario.get_email() == email:
                return usuario
        return None