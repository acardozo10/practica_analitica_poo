from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Circulo import Circulo
from Cilindro import Cilindro

nombre=input("Que figura desea usar: ")
print("la figura seleccionada es ",nombre)


cil= Cilindro("Cilindro 1")
cil.radio=20
cil.altura=50

print(cil.area())