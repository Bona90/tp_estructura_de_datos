from programa.interfaces import IEnviarMensaje, IRecibirMensajes
from programa.mensaje import Mensaje
from programa.cola_prioridad import ColaPrioridad

# Clase ServidorCorreo: gestiona usuarios y permite el envío y recepción de mensajes.
class ServidorCorreo(IEnviarMensaje, IRecibirMensajes):
    def __init__(self, nombre):
        self.set_nombre(nombre)
        self.__usuarios = []
        self.__cola_urgentes = ColaPrioridad()    #    se inicializa la cola de prioridad para manejar mensajes urgentes.
        

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
        if usuario and usuario.validar_password(password):   #    se utiliza el método público de usuario para validar la contraseña.
            return usuario
        return None

    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo, prioridad=3):  # Crea un mensaje y lo envía a "recibir_mensaje"
        mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
        if prioridad <= 2:    #    si la prioridad es 1 se agrega a la cola de mensajes urgentes.
            self.__cola_urgentes.agregar(mensaje, prioridad)
        else:    #    si la prioridad es 3 o mas, se envía de inmediato.
            self.recibir_mensaje(mensaje, destinatario)

    def recibir_mensaje(self, mensaje, destinatario):    # Busca un usuario registrado y le entrega el mensaje.
        usuario = self.buscar_usuario(destinatario)
        if usuario:
            usuario.recibir_mensaje(mensaje)    #    #El mensaje se entrega al usuario y activa la logica de filtrado.

    def procesar_cola_urgente(self):    #    procesa y entrega los mensajes de la cola de prioridad.
        mensajes_procesados = 0
        while not self.__cola_urgentes.esta_vacia():    #    mientras la cola no esté vacía extrae el mensaje más urgente.
            mensaje = self.__cola_urgentes.extraer_urgente()
            self.recibir_mensaje(mensaje, mensaje.get_destinatario())    #    entrega el mensaje al destinatario.
            mensajes_procesados += 1
        return "Mensajes urgentes entregados."
        
    def buscar_usuario(self, email):    #Busca un usuario por su email dentro de la lista de registrados
        for usuario in self.__usuarios:
            if usuario.get_email() == email:
                return usuario
        return None