from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Circulo import Circulo
from Cilindro import Cilindro
from FiguraPorContructor import FiguraPorContructor
from FigurasPorSetGet import FigurasPorSetGet
from typing import List

nombre=input("Que figura desea usar: ")
lado=float(input("Digite la longitud del lado del cuadrado"))
# calculos por constructor
mi_cuadrado=Cuadrado(lado)
mi_cuadrado.nombre=nombre

listaCuadrado:List[Cuadrado]=[]

listaCuadrado.append(mi_cuadrado)
listaCuadrado.append(mi_cuadrado)

listaFiguras:List=[]
otro_cuadrado=Cuadrado(45.7)
otro_cuadrado.nombre="otro Cuadrado"
listaFiguras.append(otro_cuadrado)
#agregar circulo
mi_circulo=Circulo(25.8)
mi_circulo.nombre="miCirculo"
listaFiguras.append(mi_circulo)
#agregar triangulao
mi_triangulo= Triangulo(45.4,25.8)
mi_triangulo.nombre="mitriangulo"
listaFiguras.append(mi_triangulo)

fpc=FiguraPorContructor(mi_cuadrado,listaCuadrado,listaFiguras)

fpc.mostrarListaCudarados()

print()

fpc.mostrarDatosListaFiguras()

print("FIGURAS POR SET Y GET")

fpsg=FigurasPorSetGet()

listaFigurasSetGet=[]
cuadrado_dos=Cuadrado(4.5)
cuadrado_dos.nombre="cuadrado2"

triangulo_dos=Triangulo(4.5,2.8)
triangulo_dos.nombre="triangulodos"

rectangulo_dos=Rectangulo(25,10.2)
rectangulo_dos.nombre="rectangulodos"

listaFigurasSetGet.append(cuadrado_dos)
listaFigurasSetGet.append(triangulo_dos)
listaFigurasSetGet.append(rectangulo_dos)

fpsg.listaFiguras=listaFigurasSetGet

fpsg.mostrarDatosListaFiguras()

