import tkinter as tk
from tkinter import ttk
from servicios.biblioteca_servicio import BibliotecaServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Biblioteca")
        self.geometry("600x400")

        # Estilo visual de la interfaz
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.servicio = BibliotecaServicio()

        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = LoginView(self, self.servicio, self.mostrar_menu_principal)

    def mostrar_menu_principal(self):
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = MainView(self, self.servicio, self.mostrar_login)

if __name__ == "__main__":
    app = App()
    app.mainloop()