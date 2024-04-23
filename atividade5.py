#Samara Araujo e Alana Soares 
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area

if __name__ == "__main__":
     triangulo1 = Triangulo(4, 5, 6)
     print("Perímetro do triângulo:", triangulo1.calcular_perimetro())
     print("Área do triângulo:", triangulo1.calcular_area())