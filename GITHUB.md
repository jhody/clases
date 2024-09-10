
#### Descargar de repositorio y subirlo a mi propio repositorio
- 1 PASO: Clonar repositorio: se descarga en una carpeta: principal

 ```
    git clone --branch fin-secicon-10 https://github.com/Klerith/angular-countries.git
 ```

- 2 PASO: Cambia al directorio del repositorio clonado
 ```
    cd angular-countries
 ```
- 3 PASO: Configura tu propio repositorio como remoto:
 ```
    git remote remove origin
    git remote add origin https://github.com/jhody/Proj_countries.git
 ```
- 4 PASO: Sube el contenido a tu repositorio:
 ```
    git push -u origin fin-secicon-10
 ```

