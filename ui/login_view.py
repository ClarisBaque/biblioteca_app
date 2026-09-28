import tkinter as tk
from tkinter import messagebox, ttk

class LoginView(tk.Frame):
    def __init__(self, parent, servicio, al_iniciar_sesion):
        super().__init__(parent)
        self.servicio = servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.pack(expand=True, fill="both")
        self.crear_widgets()

    def crear_widgets(self):
        frame_login = ttk.Frame(self, padding="20")
        frame_login.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame_login, text="Inicio de Sesión", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame_login, text="Usuario:").grid(row=1, column=0, sticky="e", pady=5)
        self.entry_usuario = ttk.Entry(frame_login)
        self.entry_usuario.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(frame_login, text="Contraseña:").grid(row=2, column=0, sticky="e", pady=5)
        self.entry_password = ttk.Entry(frame_login, show="*")
        self.entry_password.grid(row=2, column=1, pady=5, padx=5)

        btn_login = ttk.Button(frame_login, text="Ingresar", command=self.iniciar_sesion)
        btn_login.grid(row=3, column=0, columnspan=2, pady=15)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return

        if self.servicio.autenticar(usuario, password):
            self.al_iniciar_sesion()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")