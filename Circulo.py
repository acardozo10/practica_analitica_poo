from FiguraGeometrica import FiguraGeometrica
from math import pi

class Circulo(FiguraGeometrica):
    def __init__(self,radio):
        self.pi=pi
        self.radio=radio

    def area(self):
        return self.pi*self.radio**2