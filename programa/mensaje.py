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