from tkinter import *
from tkinter.ttk import Style
import Logica

ventana = Tk()
ventana.title("Integrales Múltiples")
ventana.geometry("920x580")
ventana.configure(bg="#c9eeee")

Style().configure("btnC", padding=(0, 5, 0, 5),
            font='serif 10')

#Frame1 = Frame(ventana, bg="#c9ffde", padx=10, pady=10)
#Frame1.pack(padx=10, pady=10, fill=BOTH)
FrameLeft = Frame(ventana, bg="red",padx=100)
FrameLeft.pack(fill="both",side=LEFT, expand=True)
FrameRight=Frame(ventana, bg="blue")
FrameRight.pack(fill="both", side=RIGHT, padx=100, expand=True)
FrameBtn=Frame(ventana, bg="white")
FrameBtn.pack(padx=50, fill="y", expand=True)

# Configuracion de columnas y filas para botones
Label(FrameBtn, text="Centro").pack()
Label(FrameLeft, text="Izquierda").pack()
Label(FrameRight, text="Derecha").pack()

#Label(Frame1, text="Integración por múltiples Integrales", font="Lucida 22 bold"
 #E     ,bg="#c9ffde", justify="center").pack(pady=15)



Logica.main()
ventana.mainloop() 