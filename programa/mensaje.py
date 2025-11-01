# Clase Mensaje: representa un mensaje de correo.
class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.__remitente = remitente
        self.set_destinatario(destinatario)  #  se usa doble protección.
        self.set_asunto(asunto)
        self.__cuerpo = cuerpo

    # Getters y Setters
    def get_remitente(self):
        return self.__remitente

    def get_destinatario(self):
        return self.__destinatario

    def set_destinatario(self, destinatario):
        if not isinstance(destinatario, str) or "@" not in destinatario:  #  verificación para el destinatario.
            raise ValueError ("El destinatario debe ser una cadena de carácteres y contener @.")
        self.__destinatario = destinatario

    def get_asunto(self):
        return self.__asunto

    def set_asunto(self, asunto):
        if len(asunto) == 0:  #  se verifica que el asunto no esté vacío.
            raise ValueError("El asunto no puede estar vacío.")
        self.__asunto = asunto

    def get_cuerpo(self):
        return self.__cuerpo

    # Métodos de Mensaje
    def __str__(self):      #Devuelve el mensaje en forma de texto
        return (
            "De: " + self.__remitente + "\n" 
            "Para: "+ self.__destinatario + "\n" 
            "Asunto: " + self.__asunto +"\n" 
            + self.__cuerpo
            )