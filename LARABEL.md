## LARAVEL
instalar laravel
```
#### composer global require laravel/installer

```
#### crear proyecto con laravel instalado

```
laravel new mi_proyecto
```

#### crear proyecto sin instalar laravel:
ir a la carpeta del proyecto donde desea crearse el proyecto
C://wamp64/www 
```
composer create-project laravel/laravel laravel-diez
```

abrir el proyecto en visual studio code
```
code. 
```

### ARTISAN
Artisan es la interfaz de línea de comandos de Laravel

#### ver todos los comandos
```
php artisan list
```

#### crear controladores y modelos
```
php artisan make:controller UserController

php artisan make:model NombreDelModelo
```


#### migrar base de datos
```
php artisan migrate
```

#### Ejecutar un servidor de desarrollo
```
php artisan serve
```
#### Limpieza y mantenimiento:
```
php artisan config:cache
```
### Consideraciones:
Para las vistas se nombre de esta manera

```
namefile.blade.php
```

#### web.php

importar controlardor
```
user App\Controller\UserController;
...
Router::get('/users', [UserController::class, 'index']);
```