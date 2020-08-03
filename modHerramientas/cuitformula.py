import shelve
from tkinter import messagebox


def formula(sexo_var, dni_var):

    sexo = sexo_var.get()
    dni = dni_var.get()

    if sexo == int(1):
        dni = int(dni) + int(2000000000)
    else:
        dni = int(dni) + int(2700000000)
    #print(f"El valor del dni es {dni} y el tipo de variable es {type(dni)}")
    dni = str(dni)
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in range(10):
        aux += int(dni[i]) * base [i]
    #print(aux)        
    resto = aux % 11
    if resto == 0:    
        aux = 0
        cuit = int(dni) + 300000000
        cuit = str(cuit) + str(aux)
        #print(cuit)
    elif resto == 1:
        if sexo == 1:
            aux = 9
            cuit = int(dni) + 300000000
            cuit = str(cuit) + str(aux)
        else:
            aux = 4
            cuit = int(dni) - 400000000
            cuit = str(cuit) + str(aux)
    else:
        aux = 11 - resto
        cuit = dni + str(aux) 
    # Salida desde el módulo
    print("La CUIT obtenida es en el módulo de la fórmula es:",cuit) 
    messagebox.showinfo("Resultado Exitoso", "La CUIT obtenida es \n {}".format(cuit))
    # Pase a la función que procesa el shelve
    pasedecuit(cuit)

"""
with shelve.open("modHerramientas/dbcuit") as db:
    db["cuit"] = "cuit"
    print(type(db))
"""

def pasedecuit(cuit):
    with shelve.open("modHerramientas/dbcuit") as db:
        db["cuit"] = cuit
        print("El valor del shelve a transferir es", cuit)

 