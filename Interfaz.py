from tkinter import *
from tkinter.ttk import Style
import Logica

ventana = Tk()
ventana.title("Integrales Múltiples")
ventana.geometry("920x580")
ventana.configure(bg="#c9eeee")

Style().configure("btnC", padding=(0, 5, 0, 5),
            font='serif 10')

Frame1 = Frame(ventana, bg="#c9ffde", padx=10, pady=10)

Label(Frame1, text="Integración por múltiples Integrales", font="Lucida 22 bold"
,bg="#c9ffde", justify="center").pack(pady=5)

Frame1.pack(fill=BOTH)

FrameLeft = Frame(ventana)
Label(FrameLeft, text="Izquierda").pack(padx=20, pady=20)
FrameLeft.pack(side=LEFT, expand=True, fill=BOTH)

FrameRight=Frame(ventana)
Label(FrameRight, text="Derecha").pack(padx=20, pady=20)
FrameRight.pack(side=RIGHT, expand=True, fill=BOTH)

FrameBtn=Frame(ventana)
Label(FrameBtn, text="Centro").pack(padx=20, pady=20)
FrameBtn.pack(side=RIGHT, expand=True, fill=BOTH)

# Configuracion de columnas y filas para botones

#Logica.main()
ventana.mainloop() 