# Fundamentos de interfaces gráficas de usuario con Tkinter

## Tema
Fundamentos de interfaces gráficas de usuario con Tkinter.

## Objetivo de aprendizaje
Comprender cómo una aplicación de consola puede incorporar una interfaz gráfica sin reemplazar su arquitectura. La GUI se encarga de la presentación y de los eventos, mientras que los servicios conservan la lógica del sistema y el acceso a los datos.

## Evolución del programa
- **Antes:** Usuario -> CLI -> Servicios -> Modelos -> JSON
- **Ahora:** Usuario -> GUI -> Eventos -> Servicios -> Modelos -> JSON

## Capas del proyecto
* `modelos/`: Clases que representan la información del sistema (usuarios y libros) con validaciones mediante `@property`.
* `servicios/`: Lógica de negocio y lectura/escritura en archivos JSON.
* `datos/`: Archivos JSON con información persistente.
* `ui/`: Vistas gráficas desarrolladas con Tkinter.
* `main.py`: Punto de entrada que inicializa los servicios y la interfaz gráfica.

## Requisitos
* Python 3.x
* Tkinter (incluido con Python)

## Cómo ejecutar
Desde la terminal en la carpeta raíz:
```bash
python main.py