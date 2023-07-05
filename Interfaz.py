from tkinter import *
from tkinter.ttk import Style
from PIL import ImageTk, Image
import Logica

ventana = Tk()
ventana.title("Integrales Múltiples")
ventana.geometry("970x600")
ventana.configure(bg="#FF4146")
ventana.resizable(False,False)

Expresion = StringVar()

# Preparamos imagen
imgintegral = Image.open("img\simbintegracion.png")
imgintegral2 = imgintegral.resize((192,308))
imgintegralplace = ImageTk.PhotoImage(imgintegral2)

Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

Frame1 = Frame(ventana, bg="#FF4146")
Label(Frame1, text="Integración por múltiples Integrales", font="Lucida 22 bold"
,bg="#FF4146", justify="center").pack(pady=5)
EntryIntegral = Entry(Frame1, textvariable = Expresion,
justify=CENTER, width=40, font="Lucida 25")
EntryIntegral.pack(pady=30)
Frame1.pack(fill=BOTH, padx=10, pady=(10,0))

FrameRight=Frame(ventana, bg="#4984FB")
Label(FrameRight, text="Derecha").pack(padx=20, pady=20)
FrameRight.pack(side=RIGHT, fill=BOTH, expand=TRUE,padx=(8,15), pady=(10,20))

# Colocar foto
lblimagen = Label(FrameRight, image=imgintegralplace)
#lblimagen.image = imgintegralplace
lblimagen.place(relx=.28, rely=.18)

FrameBtn = Frame(ventana)
FrameBtn.pack(anchor=N, expand=True,padx=(5,0), pady=(10,0))

# CC = ConfirmCancel
FrameCC=Frame(ventana)
FrameCC.pack(side=RIGHT, expand=True, fill=BOTH, padx=20, pady=20)

btnIntegrar = Button(FrameCC, text="Integrar")
btnIntegrar.pack(padx=7, pady=7,side=LEFT, anchor=NW)

btnClear = Button(FrameCC, text="Clear")
btnClear.pack(padx=7, pady=7,side=RIGHT, anchor=SE)

# Configuracion de columnas y filas para botones

FrameBtn.rowconfigure(0, pad=50)
FrameBtn.rowconfigure(1, pad=30)
FrameBtn.rowconfigure(2, pad=30)

FrameBtn.columnconfigure(0, pad=50)
FrameBtn.columnconfigure(1, pad=50)
FrameBtn.columnconfigure(2, pad=50)
FrameBtn.columnconfigure(3, pad=50)
FrameBtn.columnconfigure(4, pad=50)

"""
Multiplicación: btnmulti
División: btndiv
Potencia: btnpot
Raiz: btnroot
Raiz Modificable: btnrootcustom
Pi: btnpi
E: btne
seno: btnsin
coseno: btncos
tangente: btntan
secante: btnsec
cosecante: btncsc
cotangente: btncot
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
btnpot.grid(row=0, column=4)
btnroot = Button(FrameBtn, text="√", height=3, width=9, bg="light gray")
btnroot.grid(row=1, column=0)
btnrootcustom = Button(FrameBtn, text="x√", height=3, width=9, bg="light gray")
btnrootcustom.grid(row=1, column=1)
btnpi = Button(FrameBtn, text="π", height=3, width=9, bg="light gray")
btnpi.grid(row=1, column=2)



#Logica.main()
ventana.mainloop() 