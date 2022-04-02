from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import tkinter
import random
import numpy as np
import pandas as pd
from pip import main
from funci import *

ventana= Tk()
ventana.config(bg="white",bd=0)
ventana.title('Reto 2')
label= tkinter.Label(ventana, text="Reto 2 Algoritmos geneticos", bg="white", fg="#007b99", )
label.configure(font=("Bahnschrift Light bold", 19))
label.pack()
style = ttk.Style()    
settings = {"TNotebook.Tab": {"configure": {"padding": [111.2, 5],
                                            "background": "white",
                                            "font":"Helvetica, 12"
                                            }}}  
style.theme_create("mi_estilo", parent="alt", settings=settings)
style.theme_use("mi_estilo")
    
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes',padx=3, pady=10)
notebook.pressed_index = None

pesInicio = tkinter.Frame(notebook, background="white")
notebook.add(pesInicio, text="Inicio")

ent=tk.Label(ventana,text="Numero de generaciones: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ent.place(x=2, y=45)
caj = Entry(ventana, width= 53, font = ("Helvetica 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
caj.place(x=250, y=45)

#accion boton
def haga():
    e1 = ent.get()
    if not e1:
        messagebox.showerror("Error", "Ingrese una funcion")
    result = funci(e1)
    


btn = tk.Button(ventana, text="Calcular", width = "20", height = "1", command= "haga", font = ("Helvetica 14")
                        ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
btn.place(x=10, y=85)

sal=tk.Label(ventana,text="El mejor resultado es: ", width="25", height="1", font=("Helvetica 14"), bg='white')
sal.place(x=2, y=140)
#resultados
ext1_t = tk.Label(ventana,text="Leche de soya: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext1_t.place(x=250, y=140)
ext1 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext1.place(x=430, y=140)

ext2_t = tk.Label(ventana,text="Yogurt: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext2_t.place(x=450, y=140)
ext2 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext2.place(x=630, y=140)

ext3_t = tk.Label(ventana,text="Galletas: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext3_t.place(x=250, y=190)
ext3 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext3.place(x=430, y=190)

ext4_t = tk.Label(ventana,text="Manzana: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext4_t.place(x=450, y=190)
ext4 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext4.place(x=630, y=190)

ext5_t = tk.Label(ventana,text="Agua: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext5_t.place(x=250, y=240)
ext5 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext5.place(x=430, y=240)

ext6_t = tk.Label(ventana,text="Barra de chocolate: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext6_t.place(x=450, y=240)
ext6 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext6.place(x=640, y=240)

ext7_t = tk.Label(ventana,text="Pan: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext7_t.place(x=250, y=290)
ext7 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext7.place(x=420, y=290)

ext8_t = tk.Label(ventana,text="Chocorramo: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext8_t.place(x=450, y=290)
ext8 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext8.place(x=620, y=290)

ext9_t = tk.Label(ventana,text="Huevo: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext9_t.place(x=250, y=340)
ext9 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext9.place(x=420, y=340)

ext10_t = tk.Label(ventana,text="RedBull: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext10_t.place(x=450, y=340)
ext10 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext10.place(x=620, y=340)

ext11_t = tk.Label(ventana,text="Nueces: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext11_t.place(x=250, y=390)
ext11 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext11.place(x=420, y=390)

ext12_t = tk.Label(ventana,text="El peso total es: ", width="30", height="1", font=("Helvetica 14"), bg='white')
ext12_t.place(x=250, y=440)
ext12 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext12.place(x=490, y=440)

ext13_t = tk.Label(ventana,text="El total de calorias es: ", width="20", height="1", font=("Helvetica 14"), bg='white')
ext13_t.place(x=250, y=490)
ext13 = tk.Label(ventana, width="5", height="1", font=("Helvetica 14"), bg='white')
ext13.place(x=500, y=490)

w, h = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
#ventana.geometry("%dx%d+0+0" % (w, h))
ventana.geometry('900x600+500+50')
ventana.mainloop()