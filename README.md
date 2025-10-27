#  Proyecto Sistema de Correo

  INTEGRANTES DEL GRUPO:  
  Bonacorsi, Gonzalo  
  Fermini, Mara  
  Santa María, Alan

Este proyecto se desarrolla en el marco de trabajo de la materia Estructura de Datos, correspondiente a la carrera Tecnicatura Universitaria en Programación de la Universidad Nacional Almirante Brown.

El objetivo principal de este proyecto es desarrollar un sistema de mensajería o correo electrónico básico, implementenado, en esta primer instancia, clases, encapsulamiento, interfaces.

Las clases principales del proyecto son:  
  **"Servidor Correo"**: gestión de usuarios y manejo de envío y recepción de mensajes.  
  **"Usuario"**: representa a un cliente del servidor, puede enviar, recibir y ordenar mensajes.  
  **"Mensaje"**: representa un correo electrónico.  
  **"Carpeta"**: permite la organización de los mensajes.  

Las interfaces se encargan de dar un marco general a algunas funciones de las clases, indicando el comportamiento general pero no la implementación de dichos métodos.  
Las interfaces presentes son:  
  **"IEnviarMensaje"**: define la capacidad de enviar mensaje.  
  **"IRecibirMensaje"**: define la capacidad de recibir mensajes.  
  **"IListarMensajes"**: define la capacidad de listar mensajes.  

El diseño del sistema se basa en el principio de Encapsulamiento, utilizando convenciones de visibilidad y métodos de acceso, getters y setters. Esto garantiza un mayor control sobre la modificación de los datos internos y mantiene la coherencia del estado de los objetos.

Se implementó la doble proteccion en atributos criticos como nombre y email. Los setters incluyen validaciones estrictas, por ejemplo que el email contenga @, que la longitud de la contraseña sea de minimo 8 carácteres.

Se limitó el acceso a datos sensibles o estructurales:
No se implementó un get para la contraseña para no exponer el valor sensible.
No se implementó un set para la lista de usuarios en ServidorCorreo ni para la lista de mensajes en Carpeta, forzando las modificaciones solo a través de métodos controlados.

Se espera que el programa permita:  
  Registrar usuarios en el servidor.  
  Enviar y recibir mensajes.  
  Mover mensajes entre carpetas.  
  Listar los mensajes de una carpta.  

**Árbol General y Lógica Recursiva**

La clase Carpeta fue implementada como un árbol general, en el cual cada nodo puede tener una cantidad infinita de hijos, en este caso una estructura jerárquica que puede tener subcarpetas ilimitadas.
La recursividad se aplica para recorrer todo el árbol de carpetas y subcarpetas, presente en la busqueda recursiva de mensajes, utilizando los métodos de busqueda por remitente o por asunto, permitiendo recorrer los mensajes en el nodo actual de la clase carpeta y cada una de sus subcarpetas.
Los métodos que permiten crear, eliminar o agregar una subcarpeta manejan las relaciones padre-hijo para mantener la integridad del árbol.

**Análisis de complejidad algorítmica.**

El análisis de eficiencia se centra en las operaciones más comunes dentro de la clase Carpeta.
**agregar_mensaje()**: este método permite añadir un mensaje al final de la lista, su complejidad es O(1) ya que se trata de una operación directa en la lista de mensajes.
**eliminar_mensaje()**: busca y borra un mensaje que se encuentra en una carpeta, su complejidad es O(m), m es la cantidad de mensajes en la carpeta, este método debe recorrer todos los mensajes hasta encontrar el mensaje y eliminarlo.
**mover_mensaje()**: permite mover un mensaje entre dos carpetas, su complejidad es O(m)+O(1) = O(m+1), O(m) es la complejidad para eliminarlo de la carpeta original en la que se encuentra y O(1) la complejidad para agregarlo a la carpeta de destino.
**crear_subcarpeta()**: permite crear una subcarpeta siempre y cuando no este duplicada, su complejidad es O(n), n es el numero de subcarpetas en ese nivel. Se recorre la lista de subcarpetas para evitar duplicados.
**busqueda_por_remitente()**: busqueda recursiva de mensajes según el remitente en todo el árbol, su complejidad es O(m+n), siendo m el total de mensajes y n el total de subcarpetas. El método debe revisar todos los nodos y todos los mensajes del árbol.
**busqueda_por_asunto()**: busqueda recursiva de mensajes según el asunto en todo el árbol, su complejidad es O(m+n), siendo m el total de mensajes y n el total de subcarpetas. El método debe revisar todos los nodos y todos los mensajes del árbol.
**busqueda_recursiva_carpeta()**: busqueda recursiva de una carpeta, su complejidad es O(n), siendo n la cantidad de carpetas y subcarpetas.

**Manejo de casos límite y excepciones.**

El sistema de correo utiliza excepciones para garantizar la coherencia de los objetos y el manejo de entradas inválidas, mediante el uso de ValueError y TypeError, con el fin de mantener la integridad de los datos.
Dentro de la clase Carpeta podemos encontrar:
**TypeError**: el programa arroja errores de este tipo al intentar agregar un mensaje a una carpeta, si el mensaje no es instancia de la calse Mensaje; al mover un mensaje entre carpetas o crear una subcarpeta, si la carpeta buscada o que se intenta crear no es instancia de la clase Carpeta.
**ValueError**: el programa arroja errores de este tipo al modificar el nombre de la carpeta, si el nombre no es una cadena de caracteres; al querer eliminar o mover un mensaje si el mensaje no existe en la carpeta de la cual se lo quiere eliminar o mover, ya que la operación no se puede realizar; al crear o agregar una subcarpeta si la carpeta ya existe, ya que no se permite dos nodos hermanos con la misma identificación.
**Operaciones recursivas**: luego de la busqueda recursiva, por asunto o remitente, de todos los nodos, si no se encuentra el mensaje buscado se devuelve una lista vacía, con el fin de evitar errores de ejecución.

**Gráfico UML de Clases**

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
    +mover_mensaje(mensaje, nombre_carpeta_destino)
    +validar_password(password)
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
