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

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

### Uso
python main.py

### Estructura del proyecto
* 📄`main.py`: Archivo principal que contiene la lógica de la aplicación Flask (API).
* 📄`data.json`: Archivo json para almacenar a los usuarios.
* 📁`templates/`: Carpeta de los templates (html).
    * 📄`index.html`: Página Home del sistema bancario.
    * 📄`cuenta.html`: Página para mostrar cuenta de un usuario.
* 📁`static/`: Carpeta para guardar los componentes estáticos de la aplicación.
    * 📁`css/`: Carpeta para guardar todos los archivos de estilos.
        * 📄`style.css`: Archivo de CSS para los componentes.
* 📄`requirements.txt`: Archivo de texto que contiene todas las dependencias necesarias para el uso de la aplicación.
* 📄`.gitignore`: Archivo para ignorar lo innecesario al subirlo a github (Python, Flask y VisualStudioCode).
* 📄`README.md`: Archivo informativo de la aplicación, la instalación, uso y documentación.