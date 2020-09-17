from tkinter import *
from tkinter import filedialog, messagebox, Label
import shutil
import os

# ----------------------------------------Funciones--------------------------------------------

def avisoSalir():

    valor = messagebox.askokcancel("Salir de la aplicación",
                                   "¿Deseas salir de la aplicación?")
    if valor == True:
        raiz.destroy()



def cambiar_de_directorio():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    shutil.copytree(dir_path + "/tiempos", dir_path + "/dir/tiempos")
    #shutil.copy(dir_path + "/archivo.txt", "C:/Program Files/archivo.txt")

    print("Se copió el archivo con éxito.")


# -----------------------------------Variables-----------------------------------------------

color_fondo = "#FFF6C7"
color_cuadro_texto = "#E4CFB0"

# ----------------------------------- Interfaz ----------------------------------------------

raiz = Tk()
raiz.title("QhechuaDicc")
#raiz.iconbitmap("llama2.ico")
raiz.config(bg=color_fondo)
raiz.resizable(0, 0)


# ------------------------------Frame para el titulo-----------------------------------------

frameTitulo = Frame()
frameTitulo.pack()
frameTitulo.config(bg=color_fondo, width="850", height="350", bd=15)


# Frame Texto
frameTexto = Frame(frameTitulo)
frameTexto.grid(row=0, column=1)
frameTexto.config(bg=color_fondo)

titulo = Label(frameTexto, text="Tiempos")
titulo.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
titulo.config(font=('bold', 20), bg=color_fondo)
# img_portada = PhotoImage(file="llama2.ico")
# frameChico = Frame(frameTitulo, img=img_portada)
# frameChico.grid(row=0, column=1, padx=5, pady=5)

# ------------------------------Frame para el contenido-----------------------------------------

frameContenido = Frame()
frameContenido.pack()
frameContenido.config(bg=color_fondo, width="850", height="350", bd=20)


# --------------------------------------Botón----------------------------------------------

# El parámetro de relleno de la siguiente línea es explicado en la documentacion de la función buscarPalabra()
calcularBoton = Button(frameContenido, command=lambda: cambiar_de_directorio())
calcularBoton.grid(row=0, column=4, padx=5, pady=10, sticky="w")
calcularBoton.config(bg=color_fondo, relief="flat")
'''
# -----------------Cuadro donde se muestra el resultado de la búsqueda---------------------
resultado = Text(frameContenido, width=40, height=12)
resultado.grid(row=1, column=0, padx=10, pady=10, columnspan=5)
resultado.config(bg=color_cuadro_texto, font="comic", wrap=WORD)  # wrap=WORD es para que haga los saltos de línea sin
# cortar una palabra por la mitad
'''

raiz.mainloop()