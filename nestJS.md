
Hay que tener instalado node

ejecutar en consola
```bat
npm i -g @nestjs/cli
```
En visual studio code importar la extensión
TypeScript Importer


### Para migrar archivo por lote
con letras con tildes y Ñ, cambiar la base de datos a utf8 y la tabla:

convertir tabla a MyISAM
```mysql
ALTER DATABASE nombre_de_tu_base CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE cliente_tmp CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

en consola ejecutar:
```bat
C:\>chcp 65001
C:\>mysql --default-character-set=utf8mb4 -u root -p ris_externo < C:\query.sql
```