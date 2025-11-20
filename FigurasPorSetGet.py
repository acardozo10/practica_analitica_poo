from Cuadrado import Cuadrado
from typing import List
class FigurasPorSetGet:
    def __init__(self):
        pass

    @property
    def cuadrado(self)->Cuadrado:
        return self._cuadrado
    

    @cuadrado.setter
    def cuadrado(self,cuadrado:Cuadrado):
        self._cuadrado=cuadrado

    @property
    def listaFiguras(self)->List:
        return self._listaFiguras
    
    @listaFiguras.setter
    def listaFiguras(self,listaFiguras:List):
        self._listaFiguras=listaFiguras

    def mostrarDatos(self):
        print("El nombre del cuadrado por set y get es: ",self.cuadrado.nombre)
        print("Su area es: ",self.cuadrado.area())


    def mostrarDatosListaFiguras(self):
        for figura in self.listaFiguras:
            print("Nombre: ",figura.nombre, "Area: ",figura.area())