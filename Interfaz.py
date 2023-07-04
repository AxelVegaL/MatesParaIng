from tkinter import *
from tkinter.ttk import Style
import Logica

ventana = Tk()
ventana.title("Integrales Múltiples")
ventana.geometry("970x600")
ventana.configure(bg="#c9eeee")

Expresion = StringVar()

Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

Frame1 = Frame(ventana, bg="#c9ffde", padx=10, pady=10)

Label(Frame1, text="Integración por múltiples Integrales", font="Lucida 22 bold"
,bg="#c9ffde", justify="center").pack(pady=5)

EntryIntegral = Entry(Frame1, textvariable = Expresion,
justify=CENTER, width=40, font="Lucida 20")
EntryIntegral.pack(pady=30)

Frame1.pack(fill=BOTH)

FrameLeft = Frame(ventana, bg="pink")
Label(FrameLeft, text="Izquierda").pack(padx=20, pady=20)
FrameLeft.pack(side=LEFT, fill=BOTH)

FrameRight=Frame(ventana, bg="pink")
Label(FrameRight, text="Derecha").pack(padx=20, pady=20)
FrameRight.pack(side=RIGHT, fill=BOTH)

FrameBtn = Frame(ventana)
FrameBtn.pack(anchor=N, expand=True, fill=BOTH) 

# CC = ConfirmCancel
FrameCC=Frame(ventana)
FrameCC.pack(side=RIGHT, expand=True, fill=BOTH, padx=20, pady=20)

btnIntegrar = Button(FrameCC, text="Integrar")
btnIntegrar.pack(padx=7, pady=7,side=LEFT, anchor=NW)

btnClear = Button(FrameCC, text="Clear")
btnClear.pack(padx=7, pady=7,side=RIGHT, anchor=SE)

# Configuracion de columnas y filas para botones

FrameBtn.rowconfigure(0, pad=100)
FrameBtn.rowconfigure(1, pad=100)

FrameBtn.columnconfigure(0, pad=50)
FrameBtn.columnconfigure(1, pad=50)
FrameBtn.columnconfigure(2, pad=50)
FrameBtn.columnconfigure(3, pad=50)

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

btnsum = Button(FrameBtn, text="+", height=3, width=9, bg="light gray")
btnsum.grid(row=0, column=0)
btnres = Button(FrameBtn, text="-", height=3, width=9, bg="light gray")
btnres.grid(row=0, column=1)
btnmulti = Button(FrameBtn, text="*", height=3, width=9, bg="light gray")
btnmulti.grid(row=0, column=2)
btndiv = Button(FrameBtn, text="/", height=3, width=9, bg="light gray")
btndiv.grid(row=0, column=3)
btnpot = Button(FrameBtn, text="^", height=3, width=9, bg="light gray")
btnpot.grid(row=1, column=0)
btnroot = Button(FrameBtn, text="√", height=3, width=9, bg="light gray")
btnroot.grid(row=1, column=1)
btnrootcustom = Button(FrameBtn, text="x√", height=3, width=9, bg="light gray")
btnrootcustom.grid(row=1, column=2)
btnpi = Button(FrameBtn, text="π", height=3, width=9, bg="light gray")
btnpi.grid(row=1, column=3)


#Logica.main()
ventana.mainloop() 