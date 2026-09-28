import os
from modelos.usuario import Usuario
from modelos.libro import Libro
from servicios.archivo_servicio import ArchivoServicio

class BibliotecaServicio:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        self.ruta_libros = os.path.join(base_dir, "datos", "libros.json")
        
        self.usuarios = []
        self.libros = []
        self.usuario_actual = None
        
        self.cargar_datos()

    def cargar_datos(self):
        datos_usuarios = ArchivoServicio.cargar_json(self.ruta_usuarios)
        self.usuarios = [Usuario.desde_diccionario(u) for u in datos_usuarios]
        
        datos_libros = ArchivoServicio.cargar_json(self.ruta_libros)
        self.libros = [Libro.desde_diccionario(l) for l in datos_libros]

    def autenticar(self, username: str, password: str) -> bool:
        for u in self.usuarios:
            if u.username == username and u.password == password:
                self.usuario_actual = u
                return True
        return False

    def obtener_libros(self) -> list:
        return self.libros

    def obtener_usuarios(self) -> list:
        return self.usuarios