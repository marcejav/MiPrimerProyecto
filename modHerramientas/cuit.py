from tkinter import *
from modHerramientas.cuitvalidaciones import validardni, validarsexo
from modHerramientas.cuitformula import formula
import shelve


# -------------------- FUNCIONES -----------------
def ventanacuit():
    root = Toplevel()
    root.title("Herramientas - CUIT")
    root.config(bg="Snow")
    root.geometry("400x250")

    # ---------  VARIABLES ----------
    dni_var = StringVar()
    sexo_var = IntVar(value=0)
    cuit_var = StringVar()
    
    # 11111111111111 SECCION SUPERIOR 11111111111111111
    # --------- ETIQUETAS Y LLENADO DE DATOS ----------
    Nombre_label = Label(root, text="Calcular la CUIT del Cliente", bg="darkblue", fg="White", font="Raleway", width=42)
    Nombre_label.grid(column=0, row=0, padx=5, pady=10, columnspan=5, sticky="NSEW")
    
    dnilabel = Label(root, text="Documento: ")
    dnilabel.grid(row=1, column=0, padx=5, pady=5, sticky="EW")
    dni_entry = Entry(root, width=25, textvariable=dni_var)
    dni_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
    dni_entry.focus()
    
    sexolabel = Label(root, text="Sexo: ")
    sexolabel.grid(row=2, column=0, padx=5, pady=5, sticky="EW")
    sexo_Fem_radiobtn = Radiobutton(root, text="Femenino", variable=sexo_var, value=0)
    sexo_Fem_radiobtn.grid(row=2, column=1, padx=5, pady=5)
    sexo_Masc_radiobtn = Radiobutton(root, text="Masculino", variable=sexo_var, value=1)
    sexo_Masc_radiobtn.grid(row=2, column=2,padx=5, pady=5)
    
    # 2222222222222 SECCION MEDIA 22222222222222
    # ---------------- BOTONES -----------------
    Limpiarbtn = Button(root, width=10, borderwidth=4, relief=RAISED, text="Limpiar", highlightbackground="lightblue", command=lambda:limpiar(dni_var, sexo_var, cuit_var, dni_entry))
    Limpiarbtn.grid(row=3, column=1, pady=5, padx=10)
    
    Calcularbtn = Button(root, width=10, borderwidth=4, relief=RAISED, text="Calcular", highlightbackground="lightblue", command=lambda:calcularcuit(dni_var, sexo_var, cuit_var, dni_entry))
    Calcularbtn.grid(row=3, column=2, pady=5, padx=10)

    # 3333333333333 SECCION INFERIOR 33333333333333
    # ----------------- VISOR ---------------------
    cuitlabel = Label(root, text="CUIT", font="Raleway")
    cuitlabel.grid(row=5, column=0, padx=5, pady=5, sticky="EW")
    cuit_entry = Entry(root, width=25, state="readonly", textvariable=cuit_var)
    cuit_entry.grid(row=5, column=1, padx=5, pady=5, sticky="EW", columnspan=2)

    # -------------- PROTEGER LA VENTANA SECUNDARIA -----------
    root.grab_set()


def limpiar(dni_var, sexo_var, cuit_var, dni_entry):
    dni_var.set("")
    sexo_var.set(value=0)
    cuit_var.set("")
    dni_entry.focus()


def pasedecuit(cuit_var):
    with shelve.open("modHerramientas/dbcuit") as db:
        cuit = db["cuit"]        
        cuit_var.set(cuit)
        #print("El valor del shelve transferido fue",cuit_var.get())
        db.close()

   
def calcularcuit(dni_var, sexo_var,cuit_var, dni_entry):
    if validardni(dni_var) and validarsexo(sexo_var):
        formula(sexo_var, dni_var)
        pasedecuit(cuit_var)
    else:
        limpiar(dni_var, sexo_var, cuit_var, dni_entry)

