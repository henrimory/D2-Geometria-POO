#import math -> importa operações matematicas

class Circulo: # definindo a classe

    def __init__(self, raio):  # inicializando
        self.ra = raio  # passando o raio pra váriavel
        self.area = 0  # iniciando minha area sem valor
        self.perimetro = 0  # iniciando meu perimetro sem valor


    def calcularAreacirc(self): # função para calcular a area
        #self.area = math.pi * (self.raio ** 2)
        self.area = 3.14*(self.ra * self.ra)  # manipulando e calculando meus valores passando para a area
        return self.area #retornando a area para a classe de execução assim que a função é chamada

    def calculaPerimetrocirc(self):  # função para calcular o perimetro
        #self.perimetro = 2 * math.pi * math.pi * self.ra
        self.perimetro = (2 * 3.14) * self.ra  # manipulando e calculando meus valores passando para o perimetro
        return self.perimetro #retornando o perimetro para a classe de execução assim que a função é chamada


