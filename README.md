#  Proyecto Sistema de Correo

  INTEGRANTES DEL GRUPO 4:  
  Bonacorsi, Gonzalo  
  Fermini, Mara  
  Santa María, Alan

Este proyecto se desarrolla en el marco de trabajo de la materia Estructura de Datos, correspondiente a la carrera Tecnicatura Universitaria en Programación de la Universidad Nacional Almirante Brown.

**"Modelado de Clases y Encapsulamiento"**

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

**"Estructuras de Datos y Recursividad"**

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

**"Algoritmos y Funcionalidades Avanzadas"**

**Filtros Automáticos**

Se implementó una lógica de filtrasdo automático que se ejecuta cada vez que el usuario recibe un mensaje. Para esto se utiliza un diccionario que mapea el nombre de la carpeta de destino a listas de condiciones, remitente o asunto.
Al activarse un filtro, el sistema utiliza la recursividad de busqueda de carpeta para localizar la carpeta de destino en cualquier nivel del árbol antes de mover el mensaje. Si la carpeta de destino no existe, el mensaje cae de forma predeterminada en la Bandeja de Entrada.

**Cola de Prioridad**

Se implementó una clase llamada ColaPrioridad para gestionar mensajes urgentes, asegurando que se procesen antes que los mensajes "normales"(utilizando FIFO como criterio de "desempate").
Se utiliza una lista enlazada (compuesta por nodos) que almacena tuplas con la información prioridad y mensaje.
La lista enlazada fue elegida para optimizar la extracción:
El método extraer_urgente() tiene una complejidad O(1), ya que el elemento de mayor prioridad siempre esta en el puntero head.
El método agregar() tiene una complejidad O(n), ya que en el peor de los casos debe recorrer la lista enlazada para insertar el nuevo nodo en la posición correcta según la prioridad.
Para integrar la cola de prioridad al Servidor de correo se anade el atributo __cola_urgentes. El método enviar_mensaje fue modificado para aceptar el parámetro prioridad = 3, que corresponde a un mensaje no urgente, los mensajes con prioridad menor serán enviados a la cola. El nuevo método procesar_cola_urgente() extrae los mensajes en orden de urgencia y los entrega a sus destinatarios.

**Grafo: Red de Servidores de Correo**

El grafo simulará la red por la cual viajan los mensajes, los nodos serán los servidores y las aristas las conexiones, para esto se utilizó un grafo no dirigido.

**Grafo de adyacencia**: El grafo se almacena como un Diccionario de Listas de Adyacencia, donde cada clave es un objeto ServidorCorreo (el nodo) y su valor es una lista de servidores a los que está conectado (las aristas).
Se implementaron dos algorítmos de búsqueda en grafos para enconetrar la ruta de trasnferencia de mensaje:

**BFS**: búsqueda por anchura, utiliza una cola para encontrar la ruta más corta entre el servidor de origen y el de destino. Este es el método predeterminado, el valor por defecto, para que el sistema priorice encontrar la ruta más corta entre servidores.

**DFS**: búsqueda en profundidad, utiliza recursividad para encontrar cualquier ruta válida entre los servidores. Este método se plantea como una opción alternativa a la predeterminada.
El método enviar_mensaje utiliza el algoritmo seleccionado para obtener una lista ordenada de servidores, iterar sobre la lista de la ruta, simulando el paso del mensaje de servidor en servidor. Una vez que se encuentra en el último servidor, llama al método recibir_mensaje de ese servidor para que el mensaje sea finalmente entregado al usuario destinatario.

** "Interfaz de Línea de Comandos (CLI)" **

En esta última etapa todas las funcionalidades del sistema fueron integradas en una Interfaz de Línea de Comandos interactiva. Esta interfaz actúa como el módulo de control que permite al usuario interactuar con el sistema de clases.
La CLI demuestra el funcionamiento dinámico del sistema de correo, validando el Grafo de Servidores, la Cola de Prioridad, y la lógica de Login en un entorno ejecutable.

** Funcionalidades claves: **

Administración del grafo: permite agregar nuevos servidores y visualizar las conexiones de la red.
Seguridad: implementa el Login para el envío y la visualización de mensajes, utilizando el método validar_password para asegurar el encapsulamiento.
Envío de mensajes: permite especificar un usuario en la red. El sistema utiliza automáticamente el algorítmo BFS para encontrar la ruta más corta entre los servidores de origen y destino.
Visualización: permite al usuario ver los mensajes recibidos en su bandeja de entrada.

Para iniciar la interfaz de comandos y la simulación completa, ejecute el script de la aplicación desde la raíz del proyecto:

python interfaz_comandos.py


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

class Nodo {
    +datos
    -siguiente
}

class ColaPrioridad {
    -head
    +esta_vacia()
    +agregar(elemento, prioridad)
    +extraer_urgente()
    +ver_proximo()
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
ColaPrioridad "1" *-- "1" Nodo : head
Nodo "1" o-- "0..1" Nodo : siguiente


