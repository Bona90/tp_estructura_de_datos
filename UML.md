```mermaid

classDiagram
    %% Interfaces

class IEnviarMensaje {
    <<interface>>
    +enviar_mensaje(destinatario, asunto, cuerpo)
}

class IRecibirMensajes {
    <<interface>>
    +recibir_mensaje(mensaje)
}

class IListarMensajes {
    <<interface>>
    +listar_mensajes()
}

    %% Clases

class Usuario {
    -__nombre
    -__email
    -__password
    -__carpetas
    +get_nombre()
    +set_nombre(nuevo_nombre)
    +get_email()
    +set_email(nuevo_email)
    +set_password(nuevo_password)
    +get_carpetas()
    +enviar_mensaje(remitente, destinatario, asunto, cuerpo)
    +recibir_mensaje(mensaje)
    +listar_mensajes(carpeta)
    +mover_mensaje(mensaje, carpeta1, carpeta2)
}

class Mensaje {
    -__remitente
    -__destinatario
    -__asunto
    -__cuerpo
    +get_remitente()
    +get_destinatario()
    +set_destinatario(destinatario)
    +get_asunto()
    +set_asunto(asunto)
    +get_cuerpo()
    +__str__()
}

class Carpeta {
    -__nombre
    -__mensajes
    +get_nombre()
    +set_nombre(nombre)
    +get_mensajes()
    +agregar_mensaje(mensaje)
    +eliminar_mensaje(mensaje)
    +listar_mensajes()
}

class ServidorCorreo {
    -__nombre
    -__usuarios
    +get_nombre()
    +set_nombre(nuevo_nombre)
    +get_usuarios()
    +registrar_usuario(usuario)
    +login(email, password)
    +enviar_mensaje(remitente, destinatario, asunto, cuerpo)
    +recibir_mensaje(mensaje, destinatario)
    +buscar_usuario(email)
}

    %% Relaciones de implementación.

IEnviarMensaje <|.. Usuario
IRecibirMensajes <|.. Usuario
IEnviarMensaje <|.. ServidorCorreo
IRecibirMensajes <|.. ServidorCorreo
IListarMensajes <|.. Carpeta

    %% Relaciones de asociación/composición

ServidorCorreo "1" o-- "*" Usuario : gestiona
Usuario "1" o-- "*" Carpeta : tiene
Carpeta "0" o-- "*" Mensaje : contiene
