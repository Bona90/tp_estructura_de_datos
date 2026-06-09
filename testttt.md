classDiagram
    %% Relaciones de Composición (El sistema es dueño de la existencia de libros y usuarios)
    SistemaBiblioteca *-- Libro : compone_libros
    SistemaBiblioteca *-- Usuario : compone_usuarios
    
    %% Relaciones de Agregación (El préstamo asocia libros y usuarios, pero estos existen por separado)
    SistemaBiblioteca *-- Prestamo : gestiona_prestamos
    Prestamo o-- Libro : libro_prestado
    Prestamo o-- Usuario : usuario_solicitante

    %% Jerarquía de Herencia
    Libro <|-- LibroFisico : Es un
    Libro <|-- LibroDigital : Es un

    class SistemaBiblioteca {
        <<Singleton>>
        - list~Libro~ libros
        - list~Usuario~ usuarios
        - list~Prestamo~ prestamos
        + registrar_libro(libro: Libro) void
        + registrar_usuario(usuario: Usuario) void
        + realizar_prestamo(dni: str, isbn: str) void
        + registrar_devolucion(isbn: str) void
    }

    class Libro {
        <<Abstract>>
        + str titulo
        + str autor
        + str isbn
        + int anio_publicacion
        + int cant_paginas
        + bool disponible
        + obtener_formato()* str
    }

    class LibroFisico {
        + str ubicacion_estante
        + obtener_formato() str
    }

    class LibroDigital {
        + str formato_archivo
        + str url_descarga
        + obtener_formato() str
    }

    class Usuario {
        + str nombre
        + str apellido
        + str dni
        + str correo_electronico
    }

    class Prestamo {
        + Libro libro
        + Usuario usuario
        + date fecha_prestamo
        + date fecha_devolucion
        + bool activo
        + finalizar_prestamo() void
    }
