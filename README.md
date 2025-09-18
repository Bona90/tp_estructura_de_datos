#  Proyecto Sistema de Correo

#  INTEGRANTES DEL GRUPO: 
#  Bonacorsi, Gonzalo
#  Fermini, Mara
#  Santa María, Alan

Este proyecto se desarrolla en el marco de trabajo de la materia Estructura de Datos, correspondiente a la carrera Tecnicatura Universitaria en Programación de la Universidad Nacional Almirante Brown.

El objetivo principal de este proyecto es desarrollar un sistema de mensajería o correo electrónico básico, implementenado, en esta primer instancia, clases, encapsulamiento, interfaces.

Las clases principales del proyecto son:
#  "Servidor Correo": gestión de usuarios y manejo de envío y recepción de mensajes
#  "Usuario": representa a un cliente del servidor, puede enviar, recibir y ordenar mensajes
#  "Mensaje": representa un correo electrónico
#  "Carpeta": permite la organización de los mensajes

Las interfaces se encargan de dar un marco general a algunas funciones de las clases, indicando el comportamiento general pero no la implementación de dichos métodos.
Las interfaces presentes son:
#  "IEnviarMensaje": define la capacidad de enviar mensaje
#  "IRecibirMensaje": define la capacidad de recibir mensajes
#  "IListarMensajes": define la capacidad de listar mensajes

Se espera que el programa permita:
#  Registrar usuarios en el servidor
#  Enviar y recibir mensajes
#  Mover mensajes entre carpetas
#  Listar los mensajes de una carpta

En este proyecto se utilizan los conceptos básicos de Programación Orientada a Objetos