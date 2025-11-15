from programa.servidorcorreo import ServidorCorreo
from programa.usuario import Usuario
from programa.mensaje import Mensaje
from programa.red_servidores import RedServidores
from getpass import getpass #el getpass oculta los caracteres cuando escribis la cotraseña en consola

def mostrar_menu():
    print("\n||| SIMULADOR DE RED DE SERVIDORES |||")
    print("1. Agregar servidor")
    print("2. Registrar usuario en un servidor")
    print("3. Mostrar servidores y conexiones")
    print("4. Enviar mensaje")
    print("5. Ver mensajes")
    print("6. Salir")

def buscar_usuario_en_red(red, correo):
    #Busca en toda la red qué servidor contiene el usuario con ese correo.
    for servidor in red._conexiones.keys():
        usuario = servidor.get_usuario(correo)
        if usuario:
            return servidor, usuario
    return None, None

def login(red):
    #Pide correo y contraseña y valida el usuario en toda la red.
    correo = input("Correo: ").strip()
    password = getpass("Contraseña: ")
    servidor, usuario = buscar_usuario_en_red(red, correo)
    if not usuario:
        print("Usuario no encontrado en ningún servidor.")
        return None, None
    if not usuario.validar_password(password):
        print("Contraseña incorrecta.")
        return None, None
    return servidor, usuario

def main():
    red = RedServidores()
    servidores = {}

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        # Opción 1: Agregar servidor (conecta automaticamente los servidores entre si)
        if opcion == "1":
            nombre = input("Nombre del servidor: ").strip()
            if nombre in servidores:
                print("Ya existe un servidor con ese nombre.")
            else:
                servidor_nuevo = ServidorCorreo(nombre)
                servidores[nombre] = servidor_nuevo
                red.agregar_servidor(servidor_nuevo)
                print(f"Servidor '{nombre}' agregado.")
                
                # Conexión automática con todos los demás
                conexiones_realizadas = []
                for nombre_existente, servidor_existente in servidores.items():
                    if nombre != nombre_existente:
                        red.conectar(servidor_nuevo, servidor_existente)
                        conexiones_realizadas.append(nombre_existente)
                
                if conexiones_realizadas:
                    print(f"Conectado automáticamente con: {', '.join(conexiones_realizadas)}")
                else:
                    print("(Primer servidor de la red, sin conexiones automáticas)")

        # Opción 2: Registrar usuario
        elif opcion == "2":
            nombre_servidor = input("Servidor donde registrar el usuario: ").strip()
            if nombre_servidor not in servidores:
                print("Ese servidor no existe.")
                continue
            nombre = input("Nombre del usuario: ").strip()
            correo = input("Correo del usuario: ").strip()
            contraseña = getpass("Contraseña: ")
            usuario = Usuario(nombre, correo, contraseña)
            servidores[nombre_servidor].registrar_usuario(usuario)
            print(f"Usuario '{correo}' registrado en servidor '{nombre_servidor}'.")

        # Opción 3: Mostrar servidores y conexiones
        elif opcion == "3":
            print("\n||| SERVIDORES Y CONEXIONES |||")
            for serv, vecinos in red._conexiones.items():
                nombres_vecinos = [v.get_nombre() for v in vecinos]
                print(f"{serv.get_nombre()} -> {', '.join(nombres_vecinos) if vecinos else '(sin conexiones)'}")

        # Opción 4: Enviar mensaje (con login)
        elif opcion == "4":
            print("\n||| LOGIN |||")
            print("No compartas tus contraseñas con nadie")
            servidor_origen, usuario_origen = login(red)
            if not usuario_origen:
                continue

            destinatario = input("Correo destinatario: ").strip()
            asunto = input("Asunto: ").strip()
            cuerpo = input("Cuerpo del mensaje: ").strip()

            # Buscar servidor destino automáticamente
            servidor_destino, usuario_destino = buscar_usuario_en_red(red, destinatario)
            if not usuario_destino:
                print("No se encontró el destinatario en la red.")
                continue

            mensaje = Mensaje(usuario_origen.get_email(), destinatario, asunto, cuerpo)
            red.enviar_mensaje(servidor_origen, servidor_destino, mensaje, metodo="bfs")
            print(f"Mensaje enviado desde '{usuario_origen.get_email()}' hacia '{destinatario}'.")

        # Opción 5: Ver mensajes (con login)
        elif opcion == "5":
            print("\n||| LOGIN |||")
            print("No compartas tus contraseñas con nadie")
            servidor, usuario = login(red)
            if not usuario:
                continue

            mensajes = usuario.get_bandeja_entrada()
            if mensajes:
                print(f"\nBandeja de entrada de {usuario.get_email()}:")
                for i, mensaje in enumerate(mensajes, 1):
                    print(f"\n--- Mensaje {i} ---")
                    print(f"De: {mensaje.get_remitente()}")
                    print(f"Asunto: {mensaje.get_asunto()}")
                    print(f"Cuerpo: {mensaje.get_cuerpo()}")
            else:
                print("La bandeja de entrada está vacía.")

        # Opción 6: Salir
        elif opcion == "6":
            print("Saliendo del simulador...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
    