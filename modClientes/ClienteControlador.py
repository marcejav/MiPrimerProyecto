from tkinter import *

# Opción Integrada al Menú Principal
#from modClientes.Vista.ClienteVista import Vista
#from modClientes.Modelo.ClienteModelo import Modelo

# Opción Individual (no conectada al menú principal Inicio.py)
from Vista.ClienteVista import Vista
from Modelo.ClienteModelo import Modelo

class ClienteControlador:
    def __init__(self, root):
        
        self.root = root
        self.ControlVista = Vista(root)
        self.ControlModelo = Modelo()
    
        # INTEGRACION DE COMANDOS DE LA VISTA PRINCIPAL
        self.ControlVista.alta_btn.config(command=self.EnlaceAlta)
        self.ControlVista.modificacion_btn.config(command=self.ValidaModificacion)
        self.ControlVista.baja_btn.config(command=self.EnlaceBaja)
        self.ControlVista.generarpdf_btn.config(command=self.EnlaceGenerarpdf)
        #self.ControlVista.generarlog_btn.config(command=self.EnlaceGenerarlog)
        self.EnlaceMostrar()

    # FUNCIONES DE ENLACE ENTRE BOTONES
    def EnlaceMostrar(self):    
        self.ControlModelo.mostrar(self.ControlVista.tree)
    
    def EnlaceAlta(self):
        self.ControlModelo.alta(self.ControlVista.denominacion_var, self.ControlVista.documento_var, self.ControlVista.movil_var, self.ControlVista.sexo_var, self.ControlVista.cp_var, self.ControlVista.cuit_var)
        self.EnlaceMostrar()
     
    def ValidaModificacion(self):
        ID = self.ControlVista.tree.item(self.ControlVista.tree.focus())
        ValidaModifica = self.ControlModelo.validamodifica(ID)
        if ValidaModifica == True:
            self.ControlVista.VentanaEdicion()
            self.ControlVista.edicion_btn.config(command=self.EnlaceEdicion)

    def EnlaceEdicion(self):
        ID = self.ControlVista.tree.item(self.ControlVista.tree.focus())
        self.ControlModelo.editar(ID, self.ControlVista.denominacion_actualizada_var, self.ControlVista.movil_actualizado_var, self.ControlVista.cp_actualizado_var)
        self.EnlaceMostrar()
          
    def EnlaceBaja(self):
        ID = self.ControlVista.tree.item(self.ControlVista.tree.focus())
        self.ControlModelo.baja(ID)
        self.EnlaceMostrar()

    def EnlaceGenerarpdf(self):
        self.ControlModelo.generarpdf()

    def EnlaceGenerarlog(self):
        self.ControlModelo.generarlog()

    
if __name__ == '__main__':
    root = Tk()
    MiApp = ClienteControlador(root)
    root.mainloop()