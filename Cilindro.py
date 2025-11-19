from FiguraGeometrica import FiguraGeometrica
from math import pi
class Cilindro(FiguraGeometrica):
    radio:float
    altura:float
    
    def __init__(self, nombre):
        self.radio
        self.altura

    def area(self):
        return 2*pi*self.radio(self.radio*self.altura)
