# PYTHON CON RASA

### 2.1. Requisitos Previos
Antes de instalar Rasa, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior.

- pip: El gestor de paquetes de Python.

___

#### Instalar pyenv gestión de versiones 

pyenv es una herramienta muy útil para gestionar múltiples versiones de Python en tu sistema. Permite instalar y cambiar entre diferentes versiones de Python de manera fácil y rápida, pero no ve paquetes

Pyenv sólo funciona para UNIX ó MAC, para windows se usa pyenv-win

pyenv en Unix trae virtualenv por defectos para la creación de entornos, pero
pyenv-win para windows no trae virtualenv en su lugar hay que usar 'venv'(viene con la version de python 3.3) o usar el paquete 'virtualenv', lo instalamos con pip.

para esta ocación usaremos virtualenv, para instalarlo siga los siquientes pasos:

      
         pip install virtualenv

#### Instalar Anaconda
Anaconda permite crear entornos, versiones y descargar paquetes con 'conda', es mas completo, esta orientado a cientifico de datos.
Maneja paquetes diferentes a 'pip', pero tbn se pueden descargar usando el comando pip

[Descargar Anaconda desde aquí](https://www.anaconda.com/download-success)


Para este caso usaremos pyenv, pq anaconda es muy pesado para instalar
____
### Crear un Entorno en pyenv

Para crear un entorno virtual, sigue estos pasos:

1. #### Instalar pyenv-win
   
   [Página de pyenv-win](https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#)
   
   pyenv-win es la versión de pyenv adaptada para Windows. Para instalarlo, sigue estos pasos:

   - #### Instalar pyenv-win usando pip: 
      [Pasos para instalar desde Power Sell](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#powershell)
      
      comandos:

      pyenv --version

   - #### Agregar pyenv-win al PATH:
      Asegúrate de agregar las rutas de pyenv a las variables de entorno de tu sistema. Abre el Panel de Control y busca "Variables de entorno". Añade las siguientes rutas a la variable de entorno PATH:

      ```
         C:\Users\<tu_usuario>\.pyenv\pyenv-win\bin
         C:\Users\<tu_usuario>\.pyenv\pyenv-win\shims
      ```
      Para ver una lista de versiones de Python compatibles con pyenv windows:
      
      ```
      pyenv install -l
      pyenv install 3.8 //se instalara la version 3.8.10
      ```
   - ### Instalar virtualenv para crear entornos virtuales

      ```
      - establecer la version como global
      pyenv global 3.8.10
      python -m pip install virtualenv
      - saber si esta instalado la version en
      pip show virtualenv
      ```
   - ### Crear un entorno virtual con pyenv
      dirigirse a una carpeta donde se creara el entorno, abrir cmd y ejecutar:
      ```
         - primero verificar la ruta donde esta instalado la version de python q se descargo con pyenv:
         pyenv which python
         - después ejecutar:
      virtualenv -p 'C:\Users\Team CEOR\.pyenv\pyenv-win\versions\3.8.10\python.exe' myenv_chatbot_rasa
      ```
   - ### Activar el entorno virtual
      Navega al directorio donde creaste el entorno virtual.Abre el cmd y luego ejecuta:
      ```
         myenv_chatbot_rasa\Scripts\activate
      ```
      Es una buena práctica asegurarte de que pip esté actualizado antes de instalar nuevos paquetes:
      ```
         python.exe -m pip install --upgrade pip
      ```

### 2.3. Instalar Rasa

Una vez que el entorno virtual esté activado, puedes proceder a instalar Rasa

```
pip install rasa
rasa --version
```

### 2.4. Instalar Docker

   Docker es una plataforma que permite empaquetar aplicaciones y sus dependencias en contenedores. Un contenedor es una unidad estandarizada de software que se ejecuta de manera consistente en cualquier entorno.


   [Página oficial](https://www.docker.com/)

   [Descarga directa](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module&_gl=1*181zznx*_gcl_au*MzQ3MjMzMDIyLjE3MjM4Mjk5Nzg.*_ga*OTc3Mjc0NTM5LjE3MjM4Mjk5Nzg.*_ga_XJWPQMJYHQ*MTcyMzgyOTk3Ny4xLjEuMTcyMzgyOTk4My41NC4wLjA.)



## 3. Clases de RASA
### 3.1. Crear proyecto
Para crear un proyecto básico con RASA
```
rasa init
```
Durante el proceso pide especificar el directorio donde se instalara el chatbot:
C:\wamp64\www\pythonPJ\myenv_chatbot_rasa\chatbot

#### CONSIDERACIONES 
RECUERDA!!
Cada vez que quieran entrenar y ejecutar el modelo, debes abrir un cmd,
luego activar el entorno con:
```
yenv_chatbot_rasa\Scripts\activate
```

Despues profundizar con comandos cd al directorio donde se creo el proyecto con rasa y allí dentro ejecutar

```
rasa train nlu
```

### 3.2. Archivos y Carpetas Principales
Una vez creado el proyecto, verás la siguiente estructura de carpetas y archivos:
- data/nlu.yml: Contiene ejemplos de intents y entities para entrenar el modelo NLU.
- data/stories.yml: Define las stories (historias), que son ejemplos de conversaciones que el bot debe manejar.
- domain.yml: Especifica el domain del bot, que incluye los intents, entities, - slots (variables de estado), responses, y actions que el bot utilizará.
- config.yml: Contiene la configuración del pipeline para el procesamiento del lenguaje natural y el modelo de políticas de diálogo.
- actions.py: Archivo Python donde puedes definir actions (acciones) personalizadas que tu bot puede ejecutar, como llamar a una API externa o realizar cálculos.
- endpoints.yml: Configura los endpoints (puntos finales) para conectar el bot con servidores externos.

Comandos:

```
rasa train
- entrenar solo NLU
rasa train nlu
- Probar el Modelo NLU
rasa shell nlu
```
#### Descargar el lenguage español para el modelo
Para instalar el modelo de lenguaje es_core_news_md para spaCy, debes seguir unos pasos específicos. Este modelo es necesario para trabajar con textos en español utilizando spaCy. Aquí está el procedimiento completo para hacerlo:
```
pip install spacy
```


