from programa.servidorcorreo import ServidorCorreo
from programa.usuario import Usuario
from programa.mensaje import Mensaje
from programa.red_servidores import RedServidores

def main():
    #Simulacion de envios de mensajes
    #Creacion de servidores:
    servidor_a = ServidorCorreo("ServidorA")
    servidor_b = ServidorCorreo("ServidorB")
    servidor_c = ServidorCorreo("ServidorC")

    #Usuarios
    usuario1 = Usuario("Daniel", "daniel2000@gmail.com", "12345678")
    usuario2 = Usuario("Lucas", "lucas90@gmail.com", "abcd1234")

    #Registrar usuarios en los servidores
    servidor_a.registrar_usuario(usuario1)
    servidor_c.registrar_usuario(usuario2)

    #Crear la red de servidores (grafo)
    red = RedServidores()
    red.conectar(servidor_a, servidor_b)
    red.conectar(servidor_b, servidor_c)

    # Crear un mensaje
    mensaje = Mensaje(remitente="daniel2000@gmail.com", destinatario="lucas90@gmail.com",
                      asunto="Comprobantes", cuerpo="Lucas, te pido que me envíes los comprobantes por favor. Gracias")

    # Enviar el mensaje a través de la red (usando BFS o DFS)
    red.enviar_mensaje(servidor_a, servidor_c, mensaje, metodo="bfs")

if __name__ == "__main__":
    main()
