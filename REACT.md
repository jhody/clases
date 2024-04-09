# CLASE DE REACT
### subiendo clase a repositorio
### CHATGPT de ayuda para programadores https://chat.openai.com/
#### Entrar al repositorio donde se va a descargar el repositorio
    git init
    git clone https://github.com/jhody/clases.git
### Ahora entrar dentro del repositorio descargado,copiar archivo a subir y agregar archivo
    git add REACT.md
### Haciendo commit para la rama
git commit -m "Add class file React.md"

### Creando rama para hithub sin espacios
    git checkout -b "upload_files"
### Enviando archivos al repositorio
    git push -u origin upload_files

### Para forzar la salida de edicion en git se preciona ESC lueg se ingresa :q!

### para subir un archivo modificado
    git add REACT.md
    git commit -m "Datos modificados" 
    git push -u origin upload_files # para subir files a la rama upload_files
    #### si ya esta establecida la rama 
    git push

