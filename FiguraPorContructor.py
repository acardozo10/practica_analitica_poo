from Cuadrado import Cuadrado
from typing import List
class FiguraPorContructor:
    def __init__(self,cuadrado:Cuadrado,listaCuadrados:List[Cuadrado],listaFiguras:List):
        self.cuadrado=cuadrado
        self.listaCuadrados=listaCuadrados
        self.listaFiguras=listaFiguras

    def mostrarDatos(self):
        print("El nombre del cuadrado es: ",self.cuadrado.nombre)
        print("Su area es:",self.cuadrado.area())

    def mostrarDatosListaFiguras(self):
        for figuras in self.listaFiguras:
            if isinstance(figuras,Cuadrado):
                cuadro:Cuadrado=figuras
                print("Cuadrado Nombre: ",cuadro.nombre, "Area: ",cuadro.area())
            else:
                 print("Otro Nombre: ",figuras.nombre, "Area: ",figuras.area())

    def mostrarListaCudarados(self):
        for figura in self.listaCuadrados:
            miFigura:Cuadrado=figura
            print("Nombre: ",miFigura.nombre, "Area: ",miFigura.area())
