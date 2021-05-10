from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#Opción Individual
from Modelo.ModeloValidacion import validar_documento, validar_denominacion, validar_movil, validar_denominacion_actualizada, validar_movil_actualizado

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



# #######################################
# ### CREAR BASE DE DATOS CON PEEWEE ####
# #######################################

db = SqliteDatabase('/Users/marcelo/Dropbox/1. Mutual/Sistema-Mutual-BackUp/MARCELITO.db')

class Entidad(Model):
    denominacion = CharField()
    documento = CharField()
    movil = CharField()

    class Meta:
        database = db

Entidad.create_table()


class Modelo():
      
    # ##########################################
    # ####### FUNCION INTERNA LIMPIAR  #########
    # ##########################################

    # ---- LIMPIAR ENTRIES POR ALTA (OK)-----
    def limpiar(self, documento_var, movil_var, denominacion_var): 
        documento_var.set("")
        movil_var.set("")
        denominacion_var.set("")
        

    # ---- LIMPIAR ENTRIES POR MODIFICACION (OK)-----
    def limpiaractualizada(self, denominacion_actualizada_var, movil_actualizado_var):
        denominacion_actualizada_var.set("")
        movil_actualizado_var.set("")



    # ################################
    # ############ ALTA ##############
    # ################################
    
    def alta(self, denominacion_var, documento_var, movil_var):
        if validar_documento(documento_var) and validar_movil(movil_var) and validar_denominacion(denominacion_var):
            
            Eleccion = messagebox.askquestion("Alta", "EXITO. \n¿Desea dar el alta el registro\n correspondiente a\n {} ?".format(denominacion_var.get()))        
            if Eleccion == "yes":
                registro_alta = Entidad()
                registro_alta.denominacion = denominacion_var.get()
                registro_alta.documento = documento_var.get()
                registro_alta.movil = movil_var.get()
                registro_alta.save()
                #observador = ConcreteObserverAlta(self)
                #estado = True
                #self.SetEstado(estado)
            else:
                self.limpiar(documento_var, movil_var, denominacion_var)
            
        else:
            self.limpiar(documento_var, movil_var, denominacion_var)
        self.limpiar(documento_var, movil_var, denominacion_var)
    
    


    # ###############################
    # ########## CONSULTA ###########
    # ###############################

    def mostrar(self, tree):      
        # Limpiando TreeView
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento) 
        # Consultado tabla
        for dato in Entidad.select():
            tree.insert('', 0, text = (dato.id), values = (dato.denominacion, dato.documento, dato.movil, dato))


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
    def editar(self, ID, denominacion_actualizada_var, movil_actualizado_var):
        if validar_denominacion_actualizada(denominacion_actualizada_var) and validar_movil_actualizado(movil_actualizado_var):      
            seleccionado = messagebox.askquestion("Modificación", "¿Está seguro que quiere \n MODIFICAR este Registro?")    
            if seleccionado == "yes":
                iD = ID["text"]
                registro_modifica = Entidad.update(denominacion = denominacion_actualizada_var.get(), movil = movil_actualizado_var.get()).where(Entidad.id == iD)
                registro_modifica.execute()
                #observador = ConcreteObserverModifica(self)
                #estado = True
                #self.SetEstado(estado)
        self.limpiaractualizada(denominacion_actualizada_var, movil_actualizado_var)
              

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
                registro_baja = Entidad.get(id)
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