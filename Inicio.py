from tkinter import *
from PIL import Image, ImageTk
from modHerramientas.cuit import ventanacuit
### Se comentó lineas 5 y 32 para por lo menos usar módulos sin integrar
#from modClientes.ClienteControlador import ClienteControlador

class MenuPrincipal:

    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Sistema de Préstamos")
        canvas = Canvas(raiz, width="800", height="600")
        canvas.grid(columnspan=4)
        logo = Image.open('Logo-mutual.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        # 1. Crear la barra de Menús
        self.barMenu = Menu(self.root)

        # 2. Crear los Menús
        self.menuClientes = Menu(self.barMenu)
        self.menuOperacion = Menu(self.barMenu)
        self.menuCobranza = Menu(self.barMenu)
        self.menuConfiguracion = Menu(self.barMenu)
        self.menuHerramientas = Menu(self.barMenu)
        

        # 3. Crear los Comandos de los Menús
        #self.menuClientes.add_command(label="Manager de Clientes", command=ClienteControlador)
        self.menuClientes.add_command(label="ABMC de Clientes")
        
        self.menuOperacion.add_command(label="Gestión de Operaciones")
        self.menuCobranza.add_command(label="Depuración")
        self.menuCobranza.add_command(label="Imputación Masiva")
        self.menuCobranza.add_command(label="Imputación Manual")
        self.menuCobranza.add_command(label="Reintegros")
        self.menuCobranza.add_separator()
        self.menuCobranza.add_command(label="Informes")
        
        self.menuHerramientas.add_command(label="CUIT", command=ventanacuit)
        self.menuConfiguracion.add_command(label="Canales")
        self.menuConfiguracion.add_command(label="Entidades")

        # 4. Agregar los Menús a la barra de los Menús
        self.barMenu.add_cascade(label="Clientes", menu=self.menuClientes)
        self.barMenu.add_cascade(label="Operaciones", menu=self.menuOperacion)
        self.barMenu.add_cascade(label="Cobranzas", menu=self.menuCobranza) 
        self.barMenu.add_cascade(label="Configuración", menu=self.menuConfiguracion)
        self.barMenu.add_cascade(label="Herramientas", menu=self.menuHerramientas)

        # 5. Indicamos que la barra de menús estará en la ventana
        self.root.config(menu=self.barMenu)


if __name__ == '__main__':
    raiz = Tk()
    MiApp = MenuPrincipal(raiz)
    raiz.mainloop()