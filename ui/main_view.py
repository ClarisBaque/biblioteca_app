import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, parent, servicio, al_cerrar_sesion):
        super().__init__(parent)
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion

        self.pack(expand=True, fill="both")
        self.crear_widgets()

    def crear_widgets(self):
        # Barra superior con opciones visuales
        barra_nav = ttk.Frame(self, padding="5")
        barra_nav.pack(side="top", fill="x")

        ttk.Button(barra_nav, text="Libros", command=self.mostrar_libros).pack(side="left", padx=5)
        ttk.Button(barra_nav, text="Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=5)
        ttk.Button(barra_nav, text="Préstamos", command=self.mostrar_prestamos).pack(side="left", padx=5)
        ttk.Button(barra_nav, text="Ventas", command=self.mostrar_ventas).pack(side="left", padx=5)
        
        ttk.Button(barra_nav, text="Cerrar Sesión", command=self.al_cerrar_sesion).pack(side="right", padx=5)

        # Separador visual
        ttk.Separator(self, orient="horizontal").pack(fill="x")

        # Pantalla central
        self.contenedor_central = ttk.Frame(self, padding="20")
        self.contenedor_central.pack(expand=True, fill="both")

        self.mostrar_inicio()

    def limpiar_contenedor(self):
        for widget in self.contenedor_central.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenedor()
        usuario_nom = self.servicio.usuario_actual.nombre if self.servicio.usuario_actual else ""
        ttk.Label(self.contenedor_central, text=f"Bienvenido(a), {usuario_nom}", font=("Helvetica", 14)).pack(pady=20)
        ttk.Label(self.contenedor_central, text="Seleccione una opción de la barra superior.").pack()

    def mostrar_libros(self):
        self.limpiar_contenedor()
        ttk.Label(self.contenedor_central, text="Catálogo de Libros", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=5)
        
        libros = self.servicio.obtener_libros()
        for libro in libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            ttk.Label(self.contenedor_central, text=f"• [{libro.id}] {libro.titulo} - Autor: {libro.autor} ({estado})").pack(anchor="w", pady=2)

    def mostrar_usuarios(self):
        self.limpiar_contenedor()
        ttk.Label(self.contenedor_central, text="Lista de Usuarios Registrados", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=5)
        
        usuarios = self.servicio.obtener_usuarios()
        for usuario in usuarios:
            ttk.Label(self.contenedor_central, text=f"• Usuario: {usuario.username} | Nombre: {usuario.nombre} | Rol: {usuario.rol}").pack(anchor="w", pady=2)

    def mostrar_prestamos(self):
        self.limpiar_contenedor()
        ttk.Label(self.contenedor_central, text="Gestión de Préstamos", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=5)
        ttk.Label(self.contenedor_central, text="(Módulo de préstamos en desarrollo para la siguiente versión)").pack(anchor="w", pady=10)

    def mostrar_ventas(self):
        self.limpiar_contenedor()
        ttk.Label(self.contenedor_central, text="Gestión de Ventas", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=5)
        ttk.Label(self.contenedor_central, text="(Módulo de ventas en desarrollo para la siguiente versión)").pack(anchor="w", pady=10)