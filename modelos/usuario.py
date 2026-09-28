class Usuario:
    def __init__(self, username: str, password: str, nombre: str = "", rol: str = "usuario"):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if not value or not value.strip():
            raise ValueError("El nombre de usuario no puede estar vacío.")
        self._username = value.strip()

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        if not value or not value.strip():
            raise ValueError("La contraseña no puede estar vacía.")
        self._password = value.strip()

    def a_diccionario(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @staticmethod
    def desde_diccionario(datos: dict):
        return Usuario(
            username=datos.get("username", ""),
            password=datos.get("password", ""),
            nombre=datos.get("nombre", ""),
            rol=datos.get("rol", "usuario")
        )