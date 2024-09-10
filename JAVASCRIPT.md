copiar un objeto sin clonar su referencia(operador spread)
```let persona2={...persona}```
### Arrglos 
#### unshift 
inserta al inicio ```.unshift(element)```

#### slice
corta ```.slice(0,10)```

#### includes
si contiene el elemento ```.includes(cadena)```

#### findIndex
```
const indice = this.peliculas.findIndex((peliculaActual: any) => peliculaActual.titulo === pelicula.titulo);
```

#### filter
retorna una arreglo que cumple la condicion
```arreglo.filter((element) => oldelemen!=element)```

## LocalStorage
```
localStorage.setItem('history', JSON.stringify(this._tagsHistory));
if(localStorage.getItem('history)){
    JSON.parse(localStorage.getItem('history'));
}
```
