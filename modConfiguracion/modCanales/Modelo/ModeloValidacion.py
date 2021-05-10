from tkinter import messagebox
import re

def validar_documento(documento_var):
    patron = "^\d{8}$"
    cadena = documento_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR CUIT\n Sólo se admiten números\nde 8 dígitos")
        return False
    else:
        return True

def validar_denominacion(denominacion_var):
    patron = "^[A-Z,]+(?:[ ][A-Z]+)*$"
    cadena = denominacion_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR DENOMINACION\n No se admiten números ni caracteres especiales")
        return False
    else:
        return True

def validar_movil(movil_var):
    patron = "^\d{10}$"
    cadena = movil_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR MÓVIL\n Sólo se admiten números de 10 dígitos")
        return False
    else:
        return True




def validar_denominacion_actualizada(denominacion_actualizada_var):
    patron = "^[A-Z,]+(?:[ ][A-Z]+)*$"
    cadena = denominacion_actualizada_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR DENOMINACION\n No se admiten números ni caracteres especiales")
        return False
    else:
        return True

def validar_movil_actualizado(movil_actualizado_var):
    patron = "^\d{10}$"
    cadena = movil_actualizado_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR MOVIL\n Sólo se admiten números de 10 dígitos")
        return False
    else:
        return True
