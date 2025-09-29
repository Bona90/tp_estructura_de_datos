from programa.interfaces import IEnviarMensaje, IRecibirMensajes
from mensaje import Mensaje
from carpeta import Carpeta

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
