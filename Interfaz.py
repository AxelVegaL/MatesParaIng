from tkinter import *
from tkinter.ttk import Style
from PIL import ImageTk, Image
from Logica import integrate_expression

ventana = Tk()
ventana.title("Integrales Múltiples")
ventana.geometry("970x600")
ventana.configure(bg="#FF4146")
ventana.resizable(False,False)

Expresion = StringVar()
Integrada = StringVar()

lim_inf_str = StringVar()
lim_sup_str = StringVar()
isDefinida = True

# DECLARACION DE FUNCIONES
def clickmulti():
      val = "*"
      Expresion.set(Expresion.get()+val)
def clickdiv():
      val = "/"
      Expresion.set(Expresion.get()+val)
def clickpot():
      val = "**"
      Expresion.set(Expresion.get()+val)
def clickroot():
      val = "sqrt()"
      Expresion.set(Expresion.get()+val)
def clickrootcustom():
      val = "()sqrt()"
      Expresion.set(Expresion.get()+val)
def clicksin():
      val = "sin()"
      Expresion.set(Expresion.get()+val)
def clickcos():
      val = "cos()"
      Expresion.set(Expresion.get()+val)
def clicktan():
      val = "tan()"
      Expresion.set(Expresion.get()+val)
def clickcsc():
      val = "csc()"
      Expresion.set(Expresion.get()+val)
def clicksec():
      val = "sec()"
      Expresion.set(Expresion.get()+val)
def clickcot():
      val = "cot()"
      Expresion.set(Expresion.get()+val)
def clickpi():
      val = "pi"
      Expresion.set(Expresion.get()+val)
def clicklog():
      val = "ln()"
      Expresion.set(Expresion.get()+val)
      
def SubirInt():
      Expresion.set(Integrada.get())
      
def Clear():
      Expresion.set("")

def setLimites():
      lim_sup = lim_sup_str.get()
      lim_inf = lim_inf_str.get()
      print(lim_sup)
      print(lim_inf)
      
def Definido():
      EntryInf.configure(state="normal")
      EntrySup.configure(state="normal")
      isDefinida = True
      print(isDefinida)
def Indefinido():
      EntryInf.configure(state="disabled")
      EntrySup.configure(state="disabled")
      isDefinida = False
      print(isDefinida)

#QUITAR RESTRICCIONES PASO A PASO SYMPY O MATHPY y checar SPLICING

# Preparamos imagen
imgintegral = Image.open("img\simbintegracion.jpeg")
imgintegral2 = imgintegral.resize((192,308))
imgintegralplace = ImageTk.PhotoImage(imgintegral2)

Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

Frame1 = Frame(ventana, bg="#FF4146")
Label(Frame1, text="Integración por múltiples Integrales", font="Lucida 22 bold"
,bg="#FF4146", fg="white", justify="center").pack(pady=(4,6))
Frame1.pack(fill=BOTH, padx=10, pady=(10,0))

EntryIntegral = Entry(Frame1, textvariable = Expresion,
justify=CENTER, width=40, font="Lucida 25")
EntryIntegral.pack(pady=20)

#Boton Clear
btnClear = Button(Frame1, text="Clear", font="Lucida 12 bold"
                        ,command=Clear)
btnClear.place(relx=.037, rely=.573)

#Entry para el número de iteraciones
EntryIteraciones = Entry(Frame1, font="Lucida 10 bold", justify=CENTER, width=5)
EntryIteraciones.place(relx=.5, rely=.68)

#Boton Integrar
def btnIntegrar_Click():
    expression_str = Expresion.get()
    num_iterations = int(EntryIteraciones.get())  # Obtener el número de iteraciones desde el Entry
    
    try:
        result = integrate_expression(expression_str, num_iterations)
        Integrada.set(str(result))
    except Exception as e:
        Integrada.set("Error: " + str(e))

btnIntegrar = Button(Frame1, text="Integrar", font="Lucida 12 bold", command=btnIntegrar_Click)
btnIntegrar.place(relx=.91, rely=.55)


FrameRight=Frame(ventana, bg="#4984FB")
FrameRight.pack(side=RIGHT, fill=BOTH, expand=TRUE, padx=(8,15), pady=(10,20))

Label(FrameRight, text="Límites de Integración", font="Lucida 12 bold",
      fg="white", bg="#4984FB").pack(pady=(10,0))

# Colocar foto
lblimagen = Label(FrameRight, image=imgintegralplace)
lblimagen.place(relx=.22, rely=.15)

#Entries de límite inferior y superior
EntryInf = Entry(FrameRight, font="Lucida 8 bold", justify=CENTER, width=5, textvariable = lim_inf_str)
EntryInf.place(relx=.52, rely=.77)
EntrySup = Entry(FrameRight, font="Lucida 8 bold", justify=CENTER, width=5, textvariable = lim_sup_str)
EntrySup.place(relx=.62, rely=.28)

btnSET = Button(FrameRight, text="Set", font="Lucida 13 bold", command = setLimites).place(relx=.82, rely=.90)
btnINDEFINIDA = Button(FrameRight, text="Indefinida", font="Lucida 13 bold", command=Indefinido).place(relx=.05, rely=.90)
btnDEFINIDA = Button(FrameRight, text="Definida", font="Lucida 13 bold", command=Definido).place(relx=.35, rely=.90)

FrameBtn = Frame(ventana)
FrameBtn.pack(anchor=N, expand=True,padx=(5,0), pady=(10,0))

# CC = ConfirmCancel
FrameResultado=Frame(ventana)
FrameResultado.pack(expand=True, fill=BOTH, padx=10, pady=(0,20))

FrameResultado.grid_columnconfigure(0, weight=1)
FrameResultado.grid_rowconfigure(0, weight=1)

EntryResultado = Entry(FrameResultado, font="Lucida 22", justify=CENTER, textvariable = Integrada).grid(row=0, column= 0,sticky="wnes")

# Configuracion de columnas y filas para botones

FrameBtn.rowconfigure(0, pad=50)
FrameBtn.rowconfigure(1, pad=50)
FrameBtn.rowconfigure(2, pad=50)

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
seno: btnsin
coseno: btncos
tangente: btntan
secante: btnsec
cosecante: btncsc
cotangente: btncot
logaritmo: btnlog
integral múltiple: btnint
"""

btnmulti = Button(FrameBtn, text="*", height=3, width=9, bg="light gray"
                  ,command=clickmulti)
btnmulti.grid(row=0, column=0)
btndiv = Button(FrameBtn, text="/", height=3, width=9, bg="light gray"
                  ,command=clickdiv)
btndiv.grid(row=0, column=1)
btnpot = Button(FrameBtn, text="^", height=3, width=9, bg="light gray"
                  ,command=clickpot)
btnpot.grid(row=0, column=2)
btnroot = Button(FrameBtn, text="√", height=3, width=9, bg="light gray"
                  ,command=clickroot)
btnroot.grid(row=0, column=3)
btnrootcustom = Button(FrameBtn, text="x√", height=3, width=9, bg="light gray"
                  ,command=clickrootcustom)
btnrootcustom.grid(row=0, column=4)
btnsin = Button(FrameBtn, text="sin", height=3, width=9, bg="light gray"
                  ,command=clicksin)
btnsin.grid(row=1, column=0)
btncos = Button(FrameBtn, text="cos", height=3, width=9, bg="light gray"
                  ,command=clickcos)
btncos.grid(row=1, column=1)
btntan = Button(FrameBtn, text="tan", height=3, width=9, bg="light gray"
                  ,command=clicktan)
btntan.grid(row=1, column=2)
btnpi = Button(FrameBtn, text="π", height=3, width=9, bg="light gray"
                  ,command=clickpi)
btnpi.grid(row=1, column=3)
btnlog = Button(FrameBtn, text="log", height=3, width=9, bg="light gray"
                  ,command=clicklog)
btnlog.grid(row=1, column=4)
btncsc = Button(FrameBtn, text="csc", height=3, width=9, bg="light gray"
                  ,command=clickcsc)
btncsc.grid(row=2, column=0)
btnsec = Button(FrameBtn, text="sec", height=3, width=9, bg="light gray"
                  ,command=clicksec)
btnsec.grid(row=2, column=1)
btncot = Button(FrameBtn, text="cot", height=3, width=9, bg="light gray"
                  ,command=clickcot)
btncot.grid(row=2, column=2)
btnint = Button(FrameBtn, text="∫", height=3, width=9, bg="light gray"
                  ,command=SubirInt)
btnint.grid(row=2, column=4)

#Logica.main()
ventana.mainloop() 