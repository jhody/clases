## Errores de al ejecutar proyecto en angular

Descargar proyecto de git:

Ejecutar el comando :
```bat
npm install
```
Si hay problemas ejecutar:
```bat
npm install --legacy-peer-deps
```
luego ejecutar:
```bat
ng serve
```

si hay problemas de firma, abrir la consola powerSell como administrador y ejecutar el comando:
```bat
Get-ExecutionPolicy
```

```bat
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Luego aceptar con Si

si no funciona, antes de ejecutar ng serve, ingresar:
```bat
$env:NODE_OPTIONS = "--openssl-legacy-provider"
```
