from tkinter import messagebox
import re

def validar_documento(documento_var):
    patron = "^\d{7,8}$"
    cadena = documento_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR DOCUMENTO\n Sólo se admiten números\ncon un mínimo de 7 y un máximo de 8 dígitos")
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

def validar_cp(cp_var):
    patron = "^\d{4}$"
    cadena = cp_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR CODIGO POSTAL\n Se admite código de 4 dígitos")
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

def validar_cp_actualizado(cp_actualizado_var):
    patron = "^\d{4}$"
    cadena = cp_actualizado_var.get()
    if not (re.fullmatch(patron, cadena)):
        messagebox.showerror("Error", "ERROR CODIGO POSTAL\n Se admite código de 4 dígitos")
        return False
    else:
        return True