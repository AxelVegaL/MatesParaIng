from tkinter import *
from tkinter.ttk import Style
import Logica

ventana = Tk()
ventana.title("Integrales Múltiples")
ventana.geometry("920x580")
ventana.configure(bg="#c9eeee")

Expresion = StringVar()

Style().configure("btnC", padding=(0, 5, 0, 5),
            font='serif 10')

Frame1 = Frame(ventana, bg="#c9ffde", padx=10, pady=10)

Label(Frame1, text="Integración por múltiples Integrales", font="Lucida 22 bold"
,bg="#c9ffde", justify="center").pack(pady=5)

EntryIntegral = Entry(Frame1, textvariable = Expresion,
justify=CENTER, width=40, font="Lucida 20")
EntryIntegral.pack(pady=30)

Frame1.pack(fill=BOTH)

FrameLeft = Frame(ventana)
Label(FrameLeft, text="Izquierda").pack(padx=20, pady=20)
FrameLeft.pack(side=LEFT, expand=True, fill=BOTH)

FrameRight=Frame(ventana)
Label(FrameRight, text="Derecha").pack(padx=20, pady=20)
FrameRight.pack(side=RIGHT, expand=True, fill=BOTH)

FrameBtn = Frame(ventana)
FrameBtn.pack(anchor=S, expand=True, fill=BOTH)

# CC = ConfirmCancel
FrameCC=Frame(ventana)
FrameCC.pack(side=RIGHT, expand=True, fill=BOTH, padx=20, pady=20)


# Configuracion de columnas y filas para botones

FrameBtn.columnconfigure(0, pad=5)
FrameBtn.columnconfigure(1, pad=5)

FrameBtn.rowconfigure(0, pad=3)
FrameBtn.rowconfigure(1, pad=3)
FrameBtn.rowconfigure(2, pad=3)
FrameBtn.rowconfigure(3, pad=3)

"""
Suma: btnsum
Resta: btnres
Multiplicación: btnmulti
División: btndiv
Potencia: btnpot
Raiz: btnroot
Raiz Modificable: btnrootcustom
Pi: btnpi
"""

btnsum = Button(FrameBtn, text="+")
btnsum.grid(row=0, column=0)
btnres = Button(FrameBtn, text="-")
btnres.grid(row=0, column=1)
btnmulti = Button(FrameBtn, text="*")
btnmulti.grid(row=0, column=2)
btndiv = Button(FrameBtn, text="/")
btndiv.grid(row=0, column=3)
btnpot = Button(FrameBtn, text="^")
btnpot.grid(row=1, column=0)
btnroot = Button(FrameBtn, text="√")
btnroot.grid(row=1, column=1)
btnrootcustom = Button(FrameBtn, text="x√")
btnrootcustom.grid(row=1, column=2)
btnpi = Button(FrameBtn, text="π")
btnpi.grid(row=1, column=3)


#Logica.main()
ventana.mainloop() 