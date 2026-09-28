# Práctica Semana 13: Fundamentos de Interfaces Gráficas de Usuario (GUI) con Tkinter

## Información del Estudiante
* **Materia:** Programación Orientada a Objetos / Desarrollo de Software
* **Semana:** 13
* **Tema:** Incorporación de GUI con Tkinter manteniendo arquitectura en capas

---

## Descripción del Proyecto
En esta semana se integró una interfaz gráfica de usuario (GUI) basada en la librería estándar `tkinter` de Python al sistema de gestión de biblioteca existente. 

El objetivo principal es comprender cómo una aplicación de consola evoluciona hacia una interfaz visual sin romper la separación de responsabilidades ni reemplazar los servicios o persistencia de datos desarrollados en semanas anteriores.

---

## Evolución del Sistema
* **Versión Anterior (CLI):** 
  `Usuario` -> `Consola (Terminal)` -> `Servicios` -> `Modelos` -> `Archivos JSON`
* **Versión Actual (GUI Semana 13):** 
  `Usuario` -> `Interfaz Gráfica (Tkinter)` -> `Eventos (Commands)` -> `Servicios` -> `Modelos` -> `Archivos JSON`

---

## Estructura del Proyecto por Capas

```text
biblioteca_app/
│
├── datos/                  # Persistencia en archivos JSON
│   ├── libros.json
│   └── usuarios.json
│
├── modelos/                # Clases de entidad con encapsulamiento y validaciones
│   ├── __init__.py
│   ├── libro.py
│   └── usuario.py
│
├── servicios/              # Lógica de negocio y lectura/escritura de datos
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── biblioteca_servicio.py
│
├── ui/                     # Vistas y componentes de la interfaz gráfica (Tkinter)
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py                 # Ventana principal e hilo de ejecución (mainloop)
└── README.md               # Documentación formal de la entrega
