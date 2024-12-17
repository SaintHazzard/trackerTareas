# Proyecto Kivy - Aplicación Local

Este proyecto es una aplicación creada con **Kivy**, un framework de Python utilizado para el desarrollo de aplicaciones multiplataforma con interfaces gráficas. La aplicación fue desarrollada de manera local y tiene como objetivo llevar un seguimiento de las tareas completadas.


## Ejecución

Para ejecutar la aplicación, asegúrate de tener **Python** y **Kivy** instalados en tu entorno.

### Ejecución del proyecto

Clona el repositorio y navega al directorio del proyecto:

```bash
git clone https://github.com/SaintHazzard/trackerTareas
cd trackerTareasOrg
```

Ejecuta el archivo setup_env_windows.bat del proyecto

```bash
setup_env_windows.bat
```

Ejecuta el archivo main.py que funciona como puto de entrada
```bash
python3 main.py
```
## Estructura del Proyecto

```plaintext
├── controllers
│   ├── __pycache__
│   │   └── task_controller.cpython-311.pyc
│   └── task_controller.py
├── data.json
├── main.py
├── models
│   ├── __pycache__
│   │   ├── database.cpython-311.pyc
│   │   └── task_model.cpython-311.pyc
│   ├── database.py
│   └── task_model.py
├── requirements.txt
├── setup_env_windows.bat
├── sonar-project.properties
├── tasks.db
└── views
    ├── __pycache__
    │   ├── customwidgets.cpython-311.pyc
    │   ├── mainview.cpython-311.pyc
    │   └── tasklistitem.cpython-311.pyc
    ├── customwidgets.py
    ├── mainview.kv
    ├── mainview.py
    ├── tasklistitem.kv
    └── tasklistitem.py 
```

## Características Principales

- **Interfaz intuitiva** construida con Kivy.
- **Rendimiento optimizado** para sistemas locales y móviles.
- [Agrega otras características aquí]

## Ejemplo de Uso

Un ejemplo sencillo de uso de Kivy en el archivo `main.py`:

```python
from kivy.app import App
from kivy.uix.button import Button

class MiAplicacion(App):
    def build(self):
        return Button(text='Hola Mundo')

if __name__ == '__main__':
    MiAplicacion().run()
```


## Authors

- [@SaintHazzard](https://github.com/SaintHazzard)

