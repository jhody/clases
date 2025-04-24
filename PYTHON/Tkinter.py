
# EJEMPLO CON BOTONES
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.geometry('650x400+1500+200')# posicion de ventana: x=1500 y=200
ventana.resizable(0,0) # para que no se pueda redimensionar la ventana
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Métodos para colocar widgets(botones, etiquetas, entradas, etc) dentro de una ventana
.pack() # Coloca los widgets uno debajo del otro (vertical) o uno al lado del otro (horizontal).
label2.pack(side='bottom') # side='top', side='bottom', side='left', side='right'
.grid() # Organiza widgets en filas y columnas (como una tabla).
label1.grid(row=0, column=0)

# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')

# Definimos los botones
boton1 = tk.Button(ventana, text='Botón 1', width='32',height=3,bd=0,bg='#eee',cursor='hand2',command=evento1)
boton2 = tk.Button(ventana,text='/',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('/'))
boton1.grid(row=0, column=0, sticky='NSWE',
            padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)

# N(arriba), E(derecha), S(abajo), W(izquierda)
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
# boton2.grid(row=1,column=0, sticky='NSWE')

# Boton3
boton3 = ttk.Button(ventana, text='Botón 3')
# boton3.grid(row=0, column=1, sticky='NSWE')

# Boton4
boton4= tk.Button(ventana,text='Botón 4', command=evento4)
# boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()

# EJEMPLO 2
# ---------------------
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# width es la cantidad de caracteres que ocupa la caja de texto
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
# state=tk.DISABLED
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
# insert agrega un texto
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contenido
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    # Para hacer efectiva la selección del texto
    entrada1.focus()

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()

# LABEL:
# -----------
# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)
# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)
etiqueta1.config(text=entrada_var1.get())

# MESSAGEBOX:
# -----------
import tkinter as tk
from tkinter import ttk, messagebox

messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')
messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
messagebox.showwarning('Mensaje Alerta', mensaje1 + ' Alerta')

# TABULADORES O PESTAÑAS:
import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tabulador1(tabulador):
    # Agregar una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    # Agregamos un botón
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)


def crear_tabs():
    # Creamos un tab control, para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)
    # Agregamos un marco (frame) para agregar dentrol del tab y organizar elementos
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # Mostramos el tabulador
    control_tabulador.pack(fill='both')
    # control_tabulador.pack(side='bottom')
    # Creamos los componentes del tabulador1
    crear_componentes_tabulador1(tabulador1)
    # Creamos un segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido') # con LabelFrame
    control_tabulador.add(tabulador2, text='Tabulador 2')
    # Creamos los componentes del segundo tabulador
    crear_componentes_tabulador2(tabulador2)
    # Crear un tercer tabulador
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text='Tabulador 3')
    # Creamos los componentes del tercer tabulador
    crear_componentes_tabulador3(tabulador3)

    
crear_tabs()

ventana.mainloop()


# SCROLLEDTEXT: Como un textarea
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
def crear_componentes_tabulador2(tabulador):
    contenido = 'Este es mi texto con el contenido'
    # Creamos el componente de scroll
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD) # wORWD es para palabras completas
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0)

# DATALIST: Es un combobox
def crear_componentes_tabulador3(tabulador):
    # Creamos una lista usando data list comprehensions
    datos = [x+1 for x in range(100, 110)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    # Seleccionamos un elemento por default a mostrar
    combobox.current(5)
    # Agregar un boton para saber que opción seleccionó el usuario
    def mostrar_valor():
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')

    boton1 = ttk.Button(tabulador, text='Mostrar valor Seleccionado', command=mostrar_valor)
    boton1.grid(row=0, column=1)

# Componente IMAGEN
def crear_componentes_tabulador4(tabulador):
    imagen = tk.PhotoImage(file='python-logo.png')
    def mostrar_titulo():
        messagebox.showinfo('Más info imagen', f'Nombre imagen: {imagen.cget("file")}')
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    boton_imagen.grid(row=0, column=0)

# ProgressBar
def crear_componentes_tabulador5(tabulador):
    # Creamos el componente de barra de progreso
    barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    # Métodos para controlar los eventos de la barra de progreso
    def ejecutar_barra():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
            sleep(0.05)
            # Incrementamos nuestra barra de progreso
            barra_progreso['value'] = valor
            # Actualizamos la barra de progreso
            barra_progreso.update()
        barra_progreso['value'] = 0

    def ejecutar_ciclo():
        barra_progreso.start()

    def detener():
        barra_progreso.stop()

    def detener_despues():
        esperar_ms = 1000
        ventana.after(esperar_ms, barra_progreso.stop)

    # Botones para controlar los eventos de una barra de progreso
    boton_inicio = ttk.Button(tabulador,
                              text='Ejecutar Barra de Progreso', command=ejecutar_barra)
    boton_inicio.grid(row=1, column=0)
    boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
    boton_ciclo.grid(row=1, column=1)
    boton_detener = ttk.Button(tabulador, text='Detener Ejecución', command=detener)
    boton_detener.grid(row=1, column=2)
    boton_despues = ttk.Button(tabulador,
                               text='Detener Ejecución después', command=detener_despues)
    boton_despues.grid(row=1, column=3)

