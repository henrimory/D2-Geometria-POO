class Trapezio:

    def __init__(self, lado1, lado2, baseMenor, baseMaior, altura): # inicializando
        self.la1 = lado1 # passando lado pra váriavel
        self.la2 = lado2 # passando lado pra váriavel
        self.basmenor = baseMenor  #passando minha base menor pra váriavel
        self.basmaior = baseMaior   #passando minha base maior pra váriavel
        self.alt = altura   #passando minha altura pra váriavel
        self.area = 0 # iniciando minha area sem valor
        self.perimetro = 0 # iniciando meu perimetro sem valor

    def calcularAreaTrap(self): # função para calcular a area
        self.area = (self.basmaior + self.basmenor) * self.alt/2 # manipulando e calculando meus valores passando para a area
        return self.area   #retornando a area pra váriavel

    def calculaPerimetroTrap(self):  # função para calcular o perimetro
        self.perimetro = self.la1 + self.la2 + self.basmaior + self.basmenor # manipulando e calculando meus valores passando para o perimetro
        return self.perimetro    #retornando o perimetro pra váriavel