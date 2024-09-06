#### clase de angular


#### SSR (Server-Side Rendering): 
renderizar páginas web en el servidor en lugar de en el cliente

En angular: Angular Universal(conjunto de herramientas)

```
ng add @nguniversal/express-engine
```
Para REAC: Next.js o Gatsby

#### SSG (Static Site Generation) y prerendering:  

Técnicas utilizadas para generar contenido web antes de que sea solicitado por el usuario

Herramientas: Next.js, Gatsby y Jekyll

#### Prerendering:

Herramientas: Prerender.io, Angular Universal, Nuxt.js: para Vue.js

#### Ser SEO-Friendly

- Mejora del Ranking en Motores de Búsqueda
- Mayor Visibilidad y Alcance
- Mejor Experiencia del Usuario

En angular se puede usar: Angular Universal

```
ng new <nombre de la aplicación> --standalone false
```

### PARA SUBIR A PRODUCCIÓN
dentro de la carpeta del proyecto

Si se descarga desde un repositorio hay que descargar las dependencias
```npm install```

Construir la aplicación a publicar
```
ng build
ó 
npm run build
```
todo se despliega en la carpeta dist para subirlo a proudcción

- Los componentes se exportan
- Los módulos se importan

### @viewChild
Sirve para tomar referencia local
Hacer referencia a un input dentro de un componente
con @viewChild

```
1° forma
template: `
    <input type="text"
        (keyup.enter)="searchTag(txtTagInput.value)"
        #txtTagInput
    >
`
2° forma
export class SearchBoxComponent{
    @viewChild('txtTagInput')
    public tagInput!:ElementReg<HTMLInputElement>;

    searchTag(){
        const newTag = this.tagInput.nativeElement.value;
        console.log({newTag});
    }
}
```

### @viewChildren
Sirve para tomar una lista de todas las referencias locales


### Servicios
se inyecta en el componente a traves de su constructor

```constructor( private gifsService: GifsService) {}```

se llama en una funcion asi:

```this.gifsService.searchTag(newTag);```

hay que susbscribise al observable para recibir los datos

```
public countries: Country[] = [];
this.countriesService.searchCapital( term )
    .subscribe( countries => {
        this.countries = countries;
    })
```

## ngFor
lista varios elementos, repitiendo el elemento q lo contiene
<button *ngFor="let tag of tags; let indice = index">{{ tag }}</button>

## @For
@for (pelicula of peliculas; track $index){
    <p>{{$index}} Pelicula {{pelicula.titulo | uppercase}}</p>
}

tags es una funcion get en el archivo .ts, que devuelve una lista de Strings

### Pipe
Objeto que permite transformar de manera visual la información que se muestra:

uppercase
titlecase

```{{ tag | titlecase }}```


#### HttpClientModule 
Paquete para hacer peticiones
se debe importar en app.module.ts para todos

```import { HttpClientModule } from '@angular/common/http';
    .....
    imports: [
        ...
        HttpClientModule,
    ]
```
en el servicio o componente se usa en el constructor

```
constructor( private http: HttpClient ){ }
```
usar en un método

```
const params = new HttpParams()
    .set('api_key',this.apiKey)
    .set('limit','10')
    .set('q¿,tag)
this.http.get<Interfazzz>(`${this.serviceUrl}/search`,{ params })
    .subscribe( resp => {
        console.log(resp);
    });
```

### usar () y []
para eventos se usa () y para atributos []
<button (click)="searchtag(tag)" [atributo]="gifs">


### OnInit
Sirve cuando un componente se esta inicializando

```
export class CardComponent implements OnInit{

    ngOnInit(): void{
        if(!this.gif) throw new Error('Method not implementd');
    }
}
```
* Para usar el componente de un modulo en otro modulo hay que exportarlo y en el otro hay que importarlo

### ngIf
se usa una condicion

```<div *ngIf="gif.title">```
```<div *ngIf="country; else loading">```

tbn se puede hacer referencia a un template en html

```
<div *ngIf="countries.length === 0; else table">
    No hay mas registros para mostrar
</div>
<ng-template #table>
    <table>....
</ng-template>
```

### Assets
```<img src="assets/loader.svg">```

### ngStyle
```<div [ngStyle]="display:hasLoaded?'':'none'">```

### Animaciones de letras
[animate.style](https://animate.style)

### Pipes
Los pipes son funciones q se usan para darle formato a una sección en la vista

en componenetes independientes se importan desde el decorador
```
@Component({
    selector: 'app-root',
    standalone: true,
    imports: [DatePipe, UpperCasePipe, CurrencyPipe],
    ....
})
```
para usar el pile
<p>Título {{ titulo | uppercarse }}</p>
<p> Fecha Lanzamiento {{fecha | date:"dd-MMMM-yyyy" | uppercase}}</p>
<p>Precio {{ precio | currency }}</p>

## DIRECTIVAS
- Las directivas tbn se importan en un componente independiente, por ejm: NgFor
#### NgFor Y @For
```
@Component({
    selector: 'app-root',
    standalone: true,
    imports: [DatePipe, NgFor],
    ....
})
```

#### NgOptimizedImage
Optimiza las imagenes y solo se cargan las que el usuario visualiza
<link rel="preconnect" href ="https://...">

<img [ngSrc]="pelicula.poster" [priority]="$index === 0" />

#### NgIf y @If
```
@if (condicion 1)
{

}
@else if (condicion 2){

}@else if (condicion 3){

}@else{

}
```

#### Componentes 
ng generate component peliculas/listado-peliculas --skipe-tests --dry-run
--skipe-tests : para no generar el archivos de pruebas
--dry-run: solo ver los archivos que se crean sin generarlo


### @Input
Se usa en el hijo para pasar parametros desde el padre
```
@Input({required: true})
peliculas!: any[]
```

convertir el valor con una funcion transformadora
```
@Input({required: true, transform: (valor:number) => Array(valor).fill(0)})
maximoRating!:number[];
```
### @Output
Se usa en el hijo para pasar parametros hacia el padre

En el componente hijo:
```
@Output()
votado = new EventEmitter<number>();
```
para emitir el valor:
```
this.votado.emit(this.ratingValor);
```
En el componente padre:
```
<app-rating (votado)="procesarVoto($event)"></app-rating>
procesarVoto(voto:number){
    alert(`Calificación: ${voto}`);
}
```




### Variables de referencia en plantilla html
```
<input type="file" style="display:none" #cargadorArchivos>
<button (click) = "cargadorArchivos.click()">Cargar archivos</button>
```

### Proyección de contenido
 En el componente html que se va a proyectar
 ```
  <app-listado-generico [listado]="peliculas">
    <ng-container vacio>
        ....contenido html
    </ng-container>
    <ng-container contenido>
        ....contenido html
    </ng-container>
  </app-listado-generico>
  ```
 En el componente html que va a analizar la data
 ```
 <ng-content select="[vacio]"></ng-content>
 <ng-content select="[contenido]"></ng-content>
 ```
### NgClass
importarlo 
 ```
 @Component({
    imports: [NgClass]
 })

 <mat-icon [ngClass]="{nombreclase: valor>$indice}">star</mat-icon>
 ```

## Angular Material
instalarlo 
 ```
ng add @angular/material
 ```

 importando para los botones, iconos
 
 ```
 @Component({
    imports: [MatToolbarModule, MatButtonModule, MatIconModule]
 })
 <button mat-flat-button>....
 <mat-icon>delete</mat-icon>
 ```

 ## Rutas:
 en app.component.html, el router-outlet es donde se renderiza el componente
 ```
 <div class="contenedor">
    <router-outlet></router-outlet>
 </div>
 ```
En archivo app.routes.ts

 ```
export const router: Routes = [
    {path: '', component: LandingPageComponent},
    {path: 'generos', component: IndiceGenerosComponent},
    {path: 'generos/editar/:id', component: EditarGeneroComponent},
    {path: '**', redirectTo: ''}
]
 ```
Cuando se crea un archivo ts independiente para las rutas:
El forRoot es para las rutas principales y el forChild para rutas específicas para un módulo particular

 ```
@NgModule({
    imports: [
        RouterModule.forRoot( router ),
    ],
    exports:
        RouterModule
})
 ```

#### RouterLink
es el atributo con el valor del path del item del submenu
 ```
 @Component({
    imports: [RouterLink]
 })
 <a mat-button routerLink="generos">Géneros</a>
 <button mat-button routerLink="/cines/crear">Crear nuevo</button>
 ```
 Rutas por ajax
 ```
router = inject(Router);
guardarCambios(){
    //....guardar cambios
    this.router.navigate(['/generos']);
}
 ```
En el modulo del componente donde esta el submenu para usar el routerLink hay que importar el RouterModule
 ```
imports: [
    RouterModule
]
 ```
 En cada link del submenu para agregar la clase active si esta seleccionado:
 ```
<li routerLink="home" routerLinkActive="active"> Inicio</li>
 ```
Para el caso del inicio agregar routerLinkActiveOptions
 ```
<li routerLink="home" 
    routerLinkActive="active"
    [routerLinkActiveOptions]="{ exact: true }"
    > Inicio</li>
 ```
Enviar un id en el url de redirect
 ```
<a [routerLink]="['/countries/by', valor]">Ver más</a>
 ```
 #### como agregar un modulo independiente al ruteo principal?

 ```
 {
    path: 'countries',
    loadChildren: () => import('./countries/countries.module').then( m => m.CountriesModule )
 }
 ```


- Parametros URL:

Como usar variables $_GET, en el archivo app.config.ts agregar withComponentInputBinding()

 ```
providers: [provideZoneChangeDetection({eventCoalescing:true}), provideRouter(router, withComponentInputBinding()), provideAnimationAsync()]
 ```
 Ahora en el componente para recibir el valor
 ```
 @Input({transform: numberAttribute})
 id!= number;
 ```

 #### Direccionar pagina
 ```
 importar router
 constructor{
    private router: Router,
 }
...
return this.router.navigateByUrl('');
 ```

## consideraciones
 function(code:string): Observable<Country | null>{}

