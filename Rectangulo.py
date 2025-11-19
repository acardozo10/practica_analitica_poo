from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto

    def area(self):
        return self.ancho*self.alto