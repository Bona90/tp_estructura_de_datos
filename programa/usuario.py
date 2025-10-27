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
        nombre_carpeta_destino = self.__aplicar_filtro(mensaje)
        if nombre_carpeta_destino:    #    si hay un filtro a aplicar.
            carpeta_destino = None
            for carpeta_raiz in self.__carpetas:
                destino = carpeta_raiz.busqueda_recursiva_carpeta(nombre_carpeta_destino)    #   busqueda recursiva de la carpeta
                if destino:    #    
                    carpeta_destino = destino
                    break
                
            if carpeta_destino:
                carpeta_destino.agregar_mensaje(mensaje)
                return     #   el mensaje ya se agrego a la carpeta mediante el filtro aplicado
            else:
                pass  #    si la carpeta no existe se agrega a la Bandeja de Entrada.
                    
        for carpeta in self.__carpetas:
            if carpeta.get_nombre().lower() == "bandeja de entrada":    #   no se aplica ningún filtro o no existe la carpeta de destino.
                carpeta.agregar_mensaje(mensaje)
                return

    def listar_mensajes(self, carpeta):
        return carpeta.listar_mensajes()    #Pide que devuelva los mensajes que contiene la carpeta.

    def mover_mensaje(self, mensaje, nombre_carpeta_destino):
        if not isinstance(nombre_carpeta_destino, str):
            raise TypeError("El nombre de la carpeta debe ser una cadena de caracteres.")
        carpeta_origen = None    
        for carpeta_raiz in self.__carpetas:   #   iniciamos la busqueda del mensaje en la carpeta raíz.
            if mensaje in carpeta_raiz.get_mensajes():   #   se busca el mensaje en el árbol.
                carpeta_origen = carpeta_raiz
                break
        if not carpeta_origen:     #   El mensaje no está en ninguna carpeta.
            raise ValueError("El mensaje no se encuentra en ninguna carpeta del usuario.")
        carpeta_destino = None
        for carpeta_raiz in self.__carpetas:   #   localizar la carpeta de destino buscando de forma recursiva.
            destino = carpeta_raiz.busqueda_recursiva_carpeta(nombre_carpeta_destino)
            if destino:
                carpeta_destino = destino
                break
        if not carpeta_destino:
            raise ValueError("La carpeta de destino " + nombre_carpeta_destino + " no existe")
        carpeta_origen.mover_mensaje(mensaje, carpeta_destino)    #   se mueve el mensaje de la carpeta de origen a la carpeta de destino.
        return "Mensaje movido desde " + carpeta_origen.get_nombre() + " a " + carpeta_destino.get_nombre() + "."
        
    def validar_password(self, password):
        return self.__password == password    #    verificación de la contraseña sin exponer el atributo provado.
    
    def __aplicar_filtro(self, mensaje):
        from .filtros import filtros_automaticos
        remitente = mensaje.get_remitente().lower()    #    se obtienen los datos del mensaje.
        asunto = mensaje.get_asunto().lower()
        
        for nombre_carpeta, reglas in filtros_automaticos.items():
            if "remitente" in reglas:     #    se utiliza la lista de remitentes.
                for direccion in reglas["remitente"]:    #    verifica si la dirección coindice con el remitente.
                    if direccion.lower() == remitente:    #    si la dirección coincide con el remitente devuelve la carpeta.
                        return nombre_carpeta
            
            if "asunto" in reglas:    #    se utiliza la lista de asuntos.
                for palabra_clave in reglas["asunto"]:    #    verifica si la palabra clave coincide con el asunto.
                    if palabra_clave.lower() in asunto:
                        return nombre_carpeta
        return None    #    el bucle termina sin encontrar coincidencias.