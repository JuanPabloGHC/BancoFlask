# Banco Flask

Este proyecto utiliza Flask para implementar una API que simula un sistema bancario básico. Permite a los usuarios crear cuentas, iniciar sesión, realizar movimientos como depósitos, retiros y transacciones.
Además renderiza los templates directamente para visualizar el front-end.

## Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/JuanPabloGHC/BancoFlask.git

2. Accede al directorio del proyecto
    ```bash
    cd BancoFlask

3. Crea un entorno virtual (Windows)
    ```bash
    python -m venv venv

4. Activa el entorno virtual (Windows)
    ```bash
    call venv/Scripts/activate

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

### Uso
1. Correr el programa
    ```bash
    python main.py

### Estructura del proyecto
* 📄`main.py`: Archivo principal que contiene la lógica de la aplicación Flask (API).
* 📁`models`: Carpeta para guardar los modelos.
    * 📄 `Account.py`: Clase Account para una instancia de cuenta bancaria (Entradas y Salidas, Validar balance).
    * 📄 `Banco.py`: Clase Banco para una instancia de banco para gestionar cuentas (Depositos, Retiros, Transferencias, Busqueda).
* 📁`templates/`: Carpeta de los templates (html).
    * 📄`index.html`: Página Home del sistema bancario.
    * 📄`cuenta.html`: Página para mostrar cuenta de un usuario.
* 📁`static/`: Carpeta para guardar los componentes estáticos de la aplicación.
    * 📁`css/`: Carpeta para guardar todos los archivos de estilos.
        * 📄`style.css`: Archivo de CSS para los componentes.
* 📄`requirements.txt`: Archivo de texto que contiene todas las dependencias necesarias para el uso de la aplicación.
* 📄`.gitignore`: Archivo para ignorar lo innecesario al subirlo a github (Python, Flask y VisualStudioCode).
* 📄`README.md`: Archivo informativo de la aplicación, la instalación, uso y documentación.

### Dependencias
* `Flask`: Framework para el desarrollo de APIs.
* `gunicorn`: Para hacer el deploy en render.