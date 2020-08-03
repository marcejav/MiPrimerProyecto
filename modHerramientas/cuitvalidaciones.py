import re
from tkinter import messagebox

def validartitulo(titulo_var):
    patron = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    cadena = str(titulo_var.get())

    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error de Datos", "Los datos ingresados no son válidos")
        return False
    else:
        messagebox.showinfo("Validación", "Validación Exitosa!")
        return True
    
def validardni(dni_var):
    patron = "^[0-9]{7,8}$"
    cadena = str(dni_var.get())

    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error DNI", "Solo se admiten NÚMEROS. \nMínimo de 7 y máximo de 8 dígitos")
        return False
        
    else:
        print("Validación de DNI Exitosa!")
        return True

def validarsexo(sexo_var):
    patron = "^[0-1]{1}$"
    cadena = str(sexo_var.get())
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error Género", "Es obligatorio la selección del Sexo")
        return False
    else:
        print("Validación de Sexo Exitosa!")
        return True

