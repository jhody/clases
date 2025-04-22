
# EJEMPLO CON BOTONES
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')

# Definimos los botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
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

