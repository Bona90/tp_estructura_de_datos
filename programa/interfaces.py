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
