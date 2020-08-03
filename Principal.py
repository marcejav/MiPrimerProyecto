from tkinter import *
from modHerramientas.cuit import ventanacuit

class Principal:

    def __init__(self, window):
        self.root = window
        self.root.title("Menú Principal")
        self.root.config(bg="#222", width="1000", height="600")

        # 1. Crear la barra de Menús
        self.barMenu = Menu(self.root)

        # 2. Crear los Menús
        self.menuClientes = Menu(self.barMenu)
        self.menuOperacion = Menu(self.barMenu)
        self.menuCobranza = Menu(self.barMenu)
        self.menuAnalisis = Menu(self.barMenu)
        self.menuDevengamiento = Menu(self.barMenu)
        self.menuEstadistica = Menu(self.barMenu)
        self.menuHerramientas = Menu(self.barMenu)
        self.menuConfiguracion = Menu(self.barMenu)
        self.menuSalir = Menu(self.barMenu)

        # 3. Crear los Comandos de los Menús
        # 3.0. Menú Clientes
        self.menuClientes.add_command(label="Alta")
        self.menuClientes.add_command(label="Consulta")
        self.menuClientes.add_command(label="Modificación")
        self.menuClientes.add_command(label="Baja")
        self.menuClientes.add_separator()
        self.menuClientes.add_command(label="Importación")
        self.menuClientes.add_command(label="Exportación")
        self.menuClientes.add_command(label="Impresión")



        # 3.1. Menú Operaciones
        self.menuOperacion.add_command(label="Alta")
        self.menuOperacion.add_command(label="Consulta")
        self.menuOperacion.add_command(label="Modificación")
        self.menuOperacion.add_command(label="Cancelación Anticipada")
        self.menuOperacion.add_command(label="Cancelación por Consolidación")
        self.menuOperacion.add_command(label="Baja")
        self.menuOperacion.add_separator()
        self.menuOperacion.add_command(label="Importación")
        self.menuOperacion.add_command(label="Exportación")

        # 3.2. Menú Cobranzas
        self.menuCobranza.add_command(label="Depuración txt")
        self.menuCobranza.add_command(label="Imputación Ecom")
        self.menuCobranza.add_command(label="Imputación Manual")
        self.menuCobranza.add_command(label="Reintegros")
        self.menuCobranza.add_command(label="Consulta")
        self.menuCobranza.add_command(label="Cobranza por Entidad")
        self.menuCobranza.add_command(label="Pagos a Entidades")
        self.menuCobranza.add_separator()
        self.menuCobranza.add_command(label="Exportación")

        # 3.3. Menú Análisis
        self.menuAnalisis.add_command(label="Dashboard")
        self.menuAnalisis.add_command(label="Comportamiento de Pago")
        self.menuAnalisis.add_command(label="Informe de Morosidad")
        self.menuAnalisis.add_command(label="Definición de Parámetros")
        self.menuAnalisis.add_command(label="Deuda Nominal por Cliente y por Entidad")
        self.menuAnalisis.add_command(label="Cálculo de Punitorios")
        self.menuAnalisis.add_command(label="Clientes en Legales")
        self.menuAnalisis.add_separator()
        self.menuAnalisis.add_command(label="Exportación")

        # 3.4. Menú Devengamiento
        self.menuDevengamiento.add_command(label="Selección")
        self.menuDevengamiento.add_command(label="Devengamiento")
        self.menuDevengamiento.add_command(label="Consulta")
        self.menuDevengamiento.add_separator()
        self.menuDevengamiento.add_command(label="Exportación")

        # 3.5. Menú Estadística
        self.menuEstadistica.add_command(label="Extracción")
        self.menuEstadistica.add_command(label="Clasificación")
        self.menuEstadistica.add_command(label="Algoritmos")
        self.menuEstadistica.add_command(label="Regresiones")
        self.menuEstadistica.add_command(label="Correlaciones")
        self.menuEstadistica.add_separator()
        self.menuEstadistica.add_command(label="Análisis de Datos")

        # 3.6. Menú Herramientas
        self.menuHerramientas.add_command(label="CUIT", command=ventanacuit)
        self.menuHerramientas.add_command(label="BCRA")
        self.menuHerramientas.add_command(label="AFIP")
        self.menuHerramientas.add_command(label="Anses")
        self.menuHerramientas.add_command(label="Padrón Electoral")
        self.menuHerramientas.add_command(label="Bancos")
        self.menuHerramientas.add_command(label="Centrales de Información")

        # 3.7. Menú Configuración
        self.menuConfiguracion.add_command(label="Usuarios")
        self.menuConfiguracion.add_command(label="Permisos")
        self.menuConfiguracion.add_command(label="Entidades")

        # 3.8. Menú Salir
        self.menuSalir.add_command(label="Hasta Luego", command=self.root.destroy)

        # 4. Agregar los Menús a la barra de los Menús
        self.barMenu.add_cascade(label="Clientes", menu=self.menuClientes)
        self.barMenu.add_cascade(label="Operaciones", menu=self.menuOperacion)
        self.barMenu.add_cascade(label="Cobranzas", menu=self.menuCobranza)
        self.barMenu.add_cascade(label="Análisis", menu=self.menuAnalisis)
        self.barMenu.add_cascade(label="Devengamiento", menu=self.menuDevengamiento)
        self.barMenu.add_cascade(label="Estadística", menu=self.menuEstadistica)
        self.barMenu.add_cascade(label="Herramientas", menu=self.menuHerramientas)
        self.barMenu.add_cascade(label="Configuración", menu=self.menuConfiguracion)
        self.barMenu.add_cascade(label="Salir", menu=self.menuSalir)

        # 5. Indicamos que la barra de menús estará en la ventana
        self.root.config(menu=self.barMenu)

if __name__ == '__main__':
    window = Tk()
    app = Principal(window)
    window.mainloop()