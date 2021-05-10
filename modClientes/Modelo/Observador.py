import datetime
import os

def log(informe):
    archivo_log = open("./log_observador.txt", "a+")
    archivo_log.write(informe + '\n')
    #archivo_log.close()
      
class Tema():

    observadores = []

    def Agregar(self, obj):
        self.observadores.append(obj)

    def Quitar(self, obj):
        pass

    def Notificar(self, value):
        for observador in self.observadores:
            observador.Update(value)


class TemaConcreto(Tema):
    def __init__(self):
        self.estado = None

    def SetEstado(self, value):
        self.estado = value
        self.Notificar(value)

    def GetEstado(self):
        return self.estado

class Observador():
    def Update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverAlta(Observador):
    def __init__(self, obj):
        self.ObservadorAlta = obj
        self.ObservadorAlta.Agregar(self)

    def Update(self, value):
        print("Actualización dentro de ConcreteObserverAlta")
        self.estado = self.ObservadorAlta.GetEstado()
        print("Estado = ", self.estado)
        print("----------------------------------------------------")
        log_instante = str(datetime.datetime.now())
        log_mensaje = "Alta de Registro"
        informe_log = (log_instante + " - " + log_mensaje)
        print(informe_log)
        print("----------------------------------------------------")
        log(informe_log)


class ConcreteObserverBaja(Observador):
    def __init__(self, obj):
        self.ObservadorBaja = obj
        self.ObservadorBaja.Agregar(self)

    def Update(self, value):
        print("Actualización dentro de ConcreteObserverBaja")
        self.estado = self.ObservadorBaja.GetEstado()
        print("Estado = ", self.estado)
        print("----------------------------------------------------")
        log_instante = str(datetime.datetime.now())
        log_mensaje = "Baja de Registro"
        informe_log = (log_instante + " - " + log_mensaje)
        print(informe_log)
        print("----------------------------------------------------")
        log(informe_log)
        

class ConcreteObserverModifica(Observador):
    def __init__(self, obj):
        self.ObservadorModifica = obj
        self.ObservadorModifica.Agregar(self)

    def Update(self, value):
        print("Actualización dentro de ConcreteObserverModifica")
        self.estado = self.ObservadorModifica.GetEstado()
        print("Estado = ", self.estado)
        print("----------------------------------------------------")
        log_instante = str(datetime.datetime.now())
        log_mensaje = "Modificación de Registro"
        informe_log = (log_instante + " - " + log_mensaje)
        print(informe_log)
        print("----------------------------------------------------")
        log(informe_log)