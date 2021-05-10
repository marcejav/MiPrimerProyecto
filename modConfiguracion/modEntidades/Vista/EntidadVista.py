from tkinter import *
from tkinter import ttk


class Vista():

    def __init__(self, root):
        
        # --------- VENTANA PRINCIPAL ----------
        self.root = root
        self.root.title("Entidades")
        self.root.config(bg="Snow")
        self.root.geometry("820x500")
        
        # ----------- VARIABLES -------------
        self.documento_var = StringVar()
        self.denominacion_var = StringVar()
        self.movil_var = StringVar()

        # ----------- FUNCIONES -------------
        def capsdenominacion(event):
            self.denominacion_var.set(self.denominacion_var.get().upper())

        # 11111111111111111111 SUPERIOR 1111111111111111111
        # --------- ETIQUETAS E INGRESO DE DATOS ----------
        Nombre_label = Label(self.root, text="Ingrese los datos de la Entidad", bg="darkblue", fg="White", font="Raleway", width=88)
        Nombre_label.grid(column=1, row=0, padx=5, pady=10, columnspan=5, sticky="NSEW")

        Documento_label = Label(self.root, text="CUIT") 
        Documento_label.grid(column=1, row=1, padx=5, pady=5, sticky="EW")
        self.Documento_entry = Entry(self.root, textvariable=self.documento_var)
        self.Documento_entry.grid(column=2, row=1, padx=10, pady=5, columnspan=2)
        self.Documento_entry.focus()

        Movil_label = Label(self.root, text="Teléfono de Contacto") 
        Movil_label.grid(column=4, row=1, padx=10, pady=5, sticky="EW")
        self.Movil_entry = Entry(self.root, width=25, textvariable=self.movil_var)
        self.Movil_entry.grid(column=5, row=1, padx=10, pady=5, columnspan=2)

        Denominacion_label = Label(self.root, text="Denominación") 
        Denominacion_label.grid(column=1, row=2, padx=10, pady=5, sticky="EW")
        self.Denominacion_entry = Entry(self.root, width=68, textvariable=self.denominacion_var)
        self.Denominacion_entry.grid(column=2, row=2, padx=10, pady=5, columnspan=5)
        self.Denominacion_entry.bind("<KeyRelease>", capsdenominacion)
        

        # -------------------- BOTONES --------------------
        self.alta_btn = Button(self.root, width=12, borderwidth=4, relief=RAISED, text="Alta", highlightbackground="Gray")
        self.alta_btn.grid(column=1, row=10, padx=15, pady=15)
        self.modificacion_btn = Button(self.root, width=12, borderwidth=4, relief=RAISED, text="Modificación", highlightbackground="Gray")
        self.modificacion_btn.grid(column=2, row=10, padx=5, pady=15)
        self.baja_btn = Button(self.root, width=12, borderwidth=4, relief=RAISED, text="Baja", highlightbackground="Gray")
        self.baja_btn.grid(column=3, row=10, padx=5, pady=15)
        self.generarpdf_btn = Button(self.root, width=12, borderwidth=4, relief=RAISED, text="Generar PDF", highlightbackground="Gray")
        self.generarpdf_btn.grid(column=4, row=10, padx=5, pady=15)
        self.generarlog_btn = Button(self.root, width=12, borderwidth=4, relief=RAISED, text="Generar log", highlightbackground="Gray")
        self.generarlog_btn.grid(column=5, row=10, padx=10, pady=15)

        
        # ------------- TABLA VISOR DE MOVIMIENTOS  ------------
        self.tree = ttk.Treeview(self.root, height=12, columns=("#1", "#2", "#3"), selectmode="browse")
        self.tree.grid(column=1, row=12, columnspan=5)
        
        self.tree.heading('#0', anchor= CENTER, text="ID")
        self.tree.heading('#1', anchor= CENTER, text="Denominación")
        self.tree.heading('#2', anchor= CENTER, text="CUIT")
        self.tree.heading('#3', anchor= CENTER, text="Teléfono")

        self.tree.column('#0', width= 50)
        self.tree.column('#1', width= 300)
        self.tree.column('#2', width= 100)
        self.tree.column('#3', width= 100)
        
        self.scrollbar_vertical = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        #self.scrollbar_vertical.grid(column=6)
        self.tree.configure(yscrollcommand=self.scrollbar_vertical.set)

    
    def VentanaEdicion(self): 

        VentanaEdicion = Toplevel()
        # --------- VENTANA SECUNDARIA ----------
        VentanaEdicion.title("Modificación")
        VentanaEdicion.config(bg="Snow")
        VentanaEdicion.geometry("850x200")

        # ----------- VARIABLES -------------
        self.denominacion_actualizada_var = StringVar()
        self.movil_actualizado_var = StringVar()

        # ----------- FUNCIONES -------------
        def capsdenominacion(event):
           self.denominacion_actualizada_var.set(self.denominacion_actualizada_var.get().upper())
        
        # --------- ETIQUETAS E INGRESO DE DATOS ----------
        Nuevo_Nombre_label = Label(VentanaEdicion, text="Ingrese los Nuevos Datos de la Entidad", bg="darkblue", fg="White", font="Raleway", width=88)
        Nuevo_Nombre_label.grid(column=0, row=0, padx=5, pady=5, columnspan=6, sticky="NSEW")
        
        Nueva_Denominacion_label = Label(VentanaEdicion, text="Nueva Denominación") 
        Nueva_Denominacion_label.grid(column=0, row=1, padx=5, pady=5, sticky="W")
        self.Denominacion_entry = Entry(VentanaEdicion, width=68, textvariable=self.denominacion_actualizada_var)
        self.Denominacion_entry.grid(column=1, row=1, padx=5, pady=5, columnspan=6)
        self.Denominacion_entry.bind("<KeyRelease>", capsdenominacion)
        self.Denominacion_entry.focus()

        Nuevo_Movil_label = Label(VentanaEdicion, text="Nuevo Teléfono") 
        Nuevo_Movil_label.grid(column=0, row=2, padx=5, pady=5, sticky="E")
        self.Movil_entry = Entry(VentanaEdicion, width=25, textvariable=self.movil_actualizado_var)
        self.Movil_entry.grid(column=1, row=2, padx=5, pady=5, columnspan=2)
        self.Movil_entry.focus()

        # -------------------- BOTONES --------------------
        self.edicion_btn = Button(VentanaEdicion, width=10, borderwidth=8, relief=RAISED, text="Actualizar", highlightbackground="Gray")
        self.edicion_btn.grid(column=3, row=5, padx=5, pady=10)


if __name__ == '__main__':
    root = Tk()
    MiApp = Vista(root)
    root.mainloop()