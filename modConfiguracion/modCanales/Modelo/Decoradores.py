import datetime, os

# ####################
# ### DECORADORES ####
# ####################

def funcion_log(log_mensaje):
    log_instante = str(datetime.datetime.now())
    log_registro = log_instante + " - " + log_mensaje + '\n'
    print(log_registro)
    with open('log.txt', 'a+') as archivo:
        archivo.write(log_registro)

def decorador_alta(funcion):
    def funcion_envoltura(*args):
        datos = funcion(*args)
        log_mensaje = "Alta de Registro"
        funcion_log(log_mensaje)
    return funcion_envoltura

def decorador_baja(funcion):
    def funcion_envoltura(*args):
        datos = funcion(*args)
        log_mensaje = "Baja de Registro"
        funcion_log(log_mensaje)     
    return funcion_envoltura

def decorador_modifica(funcion):
    def funcion_envoltura(*args):
        datos = funcion(*args)
        log_mensaje = "Modificación de Registro"
        funcion_log(log_mensaje)     
    return funcion_envoltura
