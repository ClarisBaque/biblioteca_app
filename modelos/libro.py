class Libro:
    def __init__(self, id_libro: int, titulo: str, autor: str, disponible: bool = True):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, value: str):
        if not value or not value.strip():
            raise ValueError("El título del libro no puede estar vacío.")
        self._titulo = value.strip()

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, value: str):
        if not value or not value.strip():
            raise ValueError("El autor del libro no puede estar vacío.")
        self._autor = value.strip()

    def a_diccionario(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible
        }

    @staticmethod
    def desde_diccionario(datos: dict):
        return Libro(
            id_libro=datos.get("id", 0),
            titulo=datos.get("titulo", ""),
            autor=datos.get("autor", ""),
            disponible=datos.get("disponible", True)
        )