from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import shelve

# Opción Integrada al Menú Principal
#from modClientes.Modelo.ModeloValidacion import validar_documento, validar_denominacion, validar_movil, validar_cp, validar_denominacion_actualizada, validar_movil_actualizado, validar_cp_actualizado
#from modClientes.Modelo.ModeloCuit import calculocuit

#Opción Individual
from Modelo.ModeloValidacion import validar_documento, validar_denominacion, validar_movil, validar_cp, validar_denominacion_actualizada, validar_movil_actualizado, validar_cp_actualizado
from Modelo.ModeloCuit import calculocuit

#from Modelo.Decoradores import *
#from Modelo.Observador import *
#import re
from peewee import *
#import datetime, os
#from reportlab.platypus import SimpleDocTemplate
#from reportlab.platypus import Table
#from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter
#from reportlab.platypus import TableStyle

#cuit_var = StringVar()

def pasandocuit(cuit):
        with shelve.open("modClientes/Modelo/dbcuit") as db:            
            cuit = db["cuit"]
            #print('El valor que se recibió del shelve es ',cuit)
            cuit_var = StringVar()
            cuit_var.set(cuit)
            #print("El gran valor que se recibio del shelve es ",cuit_var.get())
            db.close()


# #######################################
# ### CREAR BASE DE DATOS CON PEEWEE ####
# #######################################

db = SqliteDatabase('/Users/marcelo/Desktop/Sistema-Mutual/BaseMutual.db')

class Cliente(Model):
    denominacion = CharField()
    documento = CharField()
    movil = CharField()
    sexo = CharField()
    cp = CharField()
    #cuit = CharField()

    class Meta:
        database = db

Cliente.create_table()


class Modelo():
      
    # ##########################################
    # ####### FUNCION INTERNA LIMPIAR  #########
    # ##########################################

    # ---- LIMPIAR ENTRIES POR ALTA (OK)-----
    def limpiar(self, documento_var, movil_var, denominacion_var, sexo_var, cp_var): 
        documento_var.set("")
        movil_var.set("")
        denominacion_var.set("")
        sexo_var.set(value=0)
        cp_var.set("")
        

    # ---- LIMPIAR ENTRIES POR MODIFICACION (OK)-----
    def limpiaractualizada(self, denominacion_actualizada_var, movil_actualizado_var, cp_actualizado_var):
        denominacion_actualizada_var.set("")
        movil_actualizado_var.set("")
        cp_actualizado_var.set("")


    # ################################
    # ############ ALTA ##############
    # ################################
    
    def alta(self, denominacion_var, documento_var, movil_var, sexo_var, cp_var, cuit_var):
        if validar_documento(documento_var) and validar_movil(movil_var) and validar_denominacion(denominacion_var) and validar_cp(cp_var):
            cuit_var = calculocuit(documento_var, sexo_var)
            pasandocuit(cuit_var)
            
            Eleccion = messagebox.askquestion("Alta", "EXITO. \n¿Desea dar el alta el registro\n correspondiente a\n {} ?".format(denominacion_var.get()))        
            if Eleccion == "yes":
                registro_alta = Cliente()
                registro_alta.denominacion = denominacion_var.get()
                registro_alta.documento = documento_var.get()
                registro_alta.movil = movil_var.get()
                registro_alta.sexo = sexo_var.get()
                registro_alta.cp = cp_var.get()
                #registro_alta.cuit = cuit_var.get()
                registro_alta.save()
                #observador = ConcreteObserverAlta(self)
                #estado = True
                #self.SetEstado(estado)
            else:
                self.limpiar(documento_var, movil_var, denominacion_var, sexo_var, cp_var)
            
        else:
            self.limpiar(documento_var, movil_var, denominacion_var, sexo_var, cp_var)
        self.limpiar(documento_var, movil_var, denominacion_var, sexo_var, cp_var)
    
    
    """
    #@decorador_alta
    def alta(self, denominacion_var, documento_var, movil_var, sexo_var, cp_var):
        if validar_documento(documento_var) and validar_movil(movil_var) and validar_denominacion(denominacion_var) and validar_cp(cp_var):
            Eleccion = messagebox.askquestion("Alta", "EXITO. \n¿Desea dar el alta el registro\n correspondiente a\n {} ?".format(denominacion_var.get()))        
            if Eleccion == "yes":
                registro_alta = Cliente()
                registro_alta.denominacion = denominacion_var.get()
                registro_alta.documento = documento_var.get()
                registro_alta.movil = movil_var.get()
                registro_alta.sexo = sexo_var.get()
                registro_alta.cp = cp_var.get()
                registro_alta.save()
                #observador = ConcreteObserverAlta(self)
                #estado = True
                #self.SetEstado(estado)
            else:
                self.limpiar(documento_var, movil_var, denominacion_var, sexo_var, cp_var)
        else:
            self.limpiar(documento_var, movil_var, denominacion_var, sexo_var, cp_var)
        self.limpiar(documento_var, movil_var, denominacion_var, sexo_var, cp_var)
    """

    # ###############################
    # ########## CONSULTA ###########
    # ###############################

    def mostrar(self, tree):      
        # Limpiando TreeView
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento) 
        # Consultado tabla
        for dato in Cliente.select():
            tree.insert('', 0, text = (dato.id), values = (dato.denominacion, dato.documento, dato.movil, dato.sexo, dato.cp, dato))


    # ###############################
    # ########## MODIFICAR ##########
    # ###############################
    
    def validamodifica(self, ID):  
        if ID ["text"] == "":
            messagebox.showerror("Error", "Elija el registro\nque quiere MODIFICAR")
            return
        else:
            id = ID["text"]
            Eleccion = messagebox.askquestion("Modificación", "Desea modificar el registro {}".format(id))        
            if Eleccion == "yes":
                #print("MODELO - El registro seleccionado es {}".format(id))
                return True
            else:
                return False

    #@decorador_modifica    
    def editar(self, ID, denominacion_actualizada_var, movil_actualizado_var, cp_actualizado_var):
        if validar_denominacion_actualizada(denominacion_actualizada_var) and validar_movil_actualizado(movil_actualizado_var) and validar_cp_actualizado(cp_actualizado_var):      
            seleccionado = messagebox.askquestion("Modificación", "¿Está seguro que quiere \n MODIFICAR este Registro?")    
            if seleccionado == "yes":
                iD = ID["text"]
                registro_modifica = Cliente.update(denominacion = denominacion_actualizada_var.get(), movil = movil_actualizado_var.get(), cp = cp_actualizado_var.get()).where(Cliente.id == iD)
                registro_modifica.execute()
                #observador = ConcreteObserverModifica(self)
                #estado = True
                #self.SetEstado(estado)
        self.limpiaractualizada(denominacion_actualizada_var, movil_actualizado_var, cp_actualizado_var)
              

    # ###############################
    # ############ BAJA #############
    # ###############################
    
    #@decorador_baja
    def baja(self, ID):
        if ID ["text"] == "":
            messagebox.showerror("Error", "Para la BAJA asegúrese siempre\nde elegir un REGISTRO")
            return
        else:
            id = ID["text"]
            seleccionado = messagebox.askquestion("Baja", "¿Está seguro que quiere \n ELIMINAR el registro {}?".format(id))    
            if seleccionado == "yes":
                registro_baja = Cliente.get(id)
                registro_baja.delete_instance()
                #observador = ConcreteObserverBaja(self)
                #estado = False
                #self.SetEstado(estado)
            

    
    # ###############################
    # ####### GENERAR PDF ###########
    # ###############################

    def generarpdf(self):
        pass
        """
        data = Cliente.select()      
        table_data = []
        for a in data:
            table_data.append([a.id, a.titulo, a.descripcion, a.fecha, a.estado])
        #print(table_data)     
        fileName = 'ReporteC.pdf'
        pdf = SimpleDocTemplate(fileName,pagesize=letter)
        table = Table(table_data)

        rowNumb = len(table_data)
        for i in range(0, rowNumb):
            if i % 2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.beige
            
            ts = TableStyle(
                [('BACKGROUND', (0,i),(-1,i), bc)]
            )
            table.setStyle(ts)

        ts = TableStyle(
            [
            ('BOX',(0,0),(-1,-1),2,colors.black),

            ('LINEBEFORE',(0,0),(-1,-1),2,colors.green),
            ('LINEABOVE',(0,0),(-1,-1),2,colors.green),

            ('GRID',(0,0),(-1,-1),2,colors.black),
            ]
        )
        table.setStyle(ts)
        elems = []
        elems.append(table)
        pdf.build(elems)
        messagebox.showinfo("Generación PDF Exitosa", "El archivo ReporteC.pdf generado \nse encuentra en la \ncarpeta principal del script.")
        """
                
    # ###############################
    # ####### GENERAR LOG ###########
    # ###############################

    def generarlog(self):
        #messagebox.showinfo("Archivo log", "El archivo log.txt generado \nse encuentra en la \ncarpeta principal del script.")
        pass