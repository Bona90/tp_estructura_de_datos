#prueba de red de servidores
from programa.servidorcorreo import ServidorCorreo
from programa.usuario import Usuario
from programa.mensaje import Mensaje
from programa.red_servidores import RedServidores
from programa.carpeta import Carpeta


def probar_red_servidores():
    
    srvA = ServidorCorreo("ServidorA")
    srvB = ServidorCorreo("ServidorB")
    srvC = ServidorCorreo("ServidorC")
    srvD = ServidorCorreo("ServidorD")

    red = RedServidores()
    red.conectar(srvA, srvB)
    red.conectar(srvB, srvC)

    usr1 = Usuario("Lucas", "lucas2020@gmail.com", "12345678")
    usr2 = Usuario("Jorge", "jorge_ff@gmail.com", "abcd1234")
    srvA.registrar_usuario(usr1)
    srvC.registrar_usuario(usr2)

    msg = Mensaje("lucas2020@gmail.com", "jorge_ff@gmail.com", "Test", "Hola Jorge")

    # BFS con ruta existente
    ruta = red.bfs(srvA, srvC)
    if ruta is not None and ruta[-1] == srvC:
        print("el metodo BFS encontró la ruta correctamente.")
    else:
        print("ERROR, el metodo BFS no encontró la ruta.")

    # Ruta inexistente
    ruta_inexistente = red.bfs(srvA, srvD)
    if ruta_inexistente is None:
        print("BFS devuelve None cuando no hay ruta.")
    else:
        print("ERROR, BFS encontró una ruta donde no debía.")

    # Envío de mensaje exitoso
    print("Simulación envío de mensaje (A a C):")
    red.enviar_mensaje(srvA, srvC, msg, metodo="bfs")

    # Envío con servidor desconectado
    print("Simulación envío de mensaje (A a D, sin conexión):")
    red.enviar_mensaje(srvA, srvD, msg, metodo="bfs")

    
#Pruebas de carpetas (recursividad)
def probar_carpetas():
    
    raiz = Carpeta("Raíz")
    sub1 = Carpeta("Sub1")
    raiz.agregar_subcarpeta(sub1)

    mensaje = Mensaje("lucas2020@gmail.com", "jorge_ff@gmail.com", "Saludo", "Hola")
    sub1.agregar_mensaje(mensaje)

    # Buscar mensaje existente
    resultado = raiz.busqueda_por_asunto("Saludo")
    if resultado is not None:
        print("La busqueda recursiva encontró el mensaje.")
    else:
        print("ERROR, no se encontró el mensaje existente.")

    # Buscar mensaje inexistente
    resultado = raiz.busqueda_por_asunto("Inexistente")
    if resultado is None:
        print("búsqueda recursiva devuelve None si no existe.")
    else:
        print("ERROR, devolvió algo cuando no debía.")

    # Carpeta vacía
    vacia = Carpeta("Vacía")
    resultado = vacia.busqueda_por_asunto("Nada")
    if resultado is None:
        print("carpeta vacía manejada correctamente.")
    else:
        print("ERROR, la carpeta vacía devolvió resultado.")

   

# --- Ejecución ---
if __name__ == "__main__":
    probar_red_servidores()
    print("\n")
    probar_carpetas()
