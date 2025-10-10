from programa.interfaces import IEnviarMensaje, IRecibirMensajes
from programa.mensaje import Mensaje
from programa.carpeta import Carpeta

#  Clase Usuario: representa a un usuario del sistema de correo.
class Usuario(IEnviarMensaje, IRecibirMensajes):
    def __init__(self, nombre, email, password):
        self.set_nombre(nombre)  #  se aplica doble protección de los atributos.
        self.set_email(email)
        self.set_password(password)
        self.__carpetas = [Carpeta("Bandeja de entrada")] #Cada usuario arranca con su carpeta "Bandeja de entrada" para que los mesajes se guarden ahi y no se pierdan.

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):  #  Se verifica que el nombre sea una cadena de carácteres.
            raise ValueError("El nombre debe ser una cadena de carácteres.")
        self.__nombre = nuevo_nombre

    def get_email(self):
        return self.__email
    
    def set_email(self, nuevo_email):
        if not isinstance(nuevo_email, str) or "@" not in nuevo_email:  #  se verifica que el email sea cadena de caracteres y contenga @.
            raise ValueError("El email debe ser una cadena de carácteres y contener @.")
        self.__email = nuevo_email

    def set_password(self, nuevo_password):
        if len(nuevo_password) < 8:  #  se verifica que la contraseña tenga una longitud mínima de 8 caracteres.
            raise ValueError("La contraseña debe tener como mínimo 8 carácteres.")
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
        if not isinstance(carpeta1, Carpeta) or not isinstance(carpeta2, Carpeta):
            raise TypeError("Las carpetas deben ser objetos carpeta.")
        if mensaje in carpeta1.get_mensajes():  #Aca podemos mover mensajes entre carpetas, para por ejemplo mandar un mensaje a una carpeta "Spam"
            carpeta1.eliminar_mensaje(mensaje)
            carpeta2.agregar_mensaje(mensaje)
            return "Mensaje movido desde " + carpeta1.get_nombre() + " a" + carpeta2.get_nombre() + "."
        else:
            raise ValueError("El mensaje no se encuentra en la carpeta.")