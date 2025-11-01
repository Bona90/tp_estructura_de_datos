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

class ColaPrioridad {
    -__cola
    +esta_vacia()
    +agregar(elemento, prioridad)
    +extraer_urgente()
    +ver_proximo()
    +__len__()
}

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
    +enviar_mensaje(remitente, destinatario, asunto, cuerpo, prioridad = 3)
    +recibir_mensaje(mensaje)
    +listar_mensajes(carpeta)
    +mover_mensaje(mensaje, nombre_carpeta_destino)
    +validar_password(password)
    -__aplicar_filtro(mensaje)
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
    -__subcarpetas : list<Carpeta>
    -__padre : Carpeta
    +get_nombre()
    +set_nombre(nombre)
    +get_mensajes()
    +get_subcarpetas()
    +get_padre()
    +set_padre(padre)
    +agregar_mensaje(mensaje)
    +eliminar_mensaje(mensaje)
    +listar_mensajes()
    +mover_mensaje(mensaje, carpeta_destino)
    +crear_subcarpeta(nombre)
    +agregar_subcarpeta(carpeta)
    +eliminar_subcarpeta(nombre)
    +busqueda_por_remitente(remitente)
    +busqueda_por_asunto(asunto)
    +busqueda_recursiva_carpeta(nombre_carpeta)
}

Carpeta "1" o-- "0..*" Carpeta

class ServidorCorreo {
    -__nombre
    -__usuarios
    -__cola_urgentes
    +get_nombre()
    +set_nombre(nuevo_nombre)
    +get_usuarios()
    +registrar_usuario(usuario)
    +login(email, password)
    +enviar_mensaje(remitente, destinatario, asunto, cuerpo, prioridad = 3)
    +recibir_mensaje(mensaje, destinatario)
    +procesar_cola_urgente()
    +buscar_usuario(email)
}

class RedServidores{
    -__grafo
    +agregar_servidor(servidor)
    +conectar(servidor1, servidor2)
    +bfs(origen, destino)
    +dfs(origen, destino)
    +enviar_mensaje(origen, destino, mensaje, metodo)
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
ServidorCorreo "1" *-- "1" ColaPrioridad : utiliza
ColaPrioridad "0" o-- "*" Mensaje : contiene
RedServidores "1" o-- "*" ServidorCorreo : contiene nodo
