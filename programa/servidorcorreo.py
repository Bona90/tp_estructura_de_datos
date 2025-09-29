from programa.interfaces import IEnviarMensaje, IRecibirMensajes
from mensaje import Mensaje

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