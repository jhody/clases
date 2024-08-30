## Clase de TypeScript`
```
const name = 'Strider';
const name2: string = 'Strider';
let hpPoints: number | string = 95;
let hpPoints2: number | 'FULL' = 95;
export class Person{
    public name: string;
    private address: string;
    constructor(){
        this.name= 'Yhody';
        this.address = 'Trujillo';
    }
}
export class Person{
    constructor(
        public name: string,
        private address: string = 'No Address'
    ){}
}
//extender
export class Hero extends Person{
    constructor(
        public alterEgo:string,
        public age:number,
        public realName:string,
    ){
        super(realName, 'New York');
    }
}
export function whatsMyType<T>(argument:T):T{

}
let var1 = whatsMyType<string>('Hola Mundo');
let var2 = whatsMyType<number>(100);
let var3 = whatsMyType<number[]>([1,2,3,4,5]);
```
ir a tsconfig.json

agregar en compilerOptions:

   "experimentalDecorators":true

? pregunta si existe
! confia en mi, q si existe