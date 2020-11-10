class Retangulo: # definindo a classe

    def __init__(self, base, altura): # inicializando
        self.la1 = base # passando minha base pra váriavel
        self.la2 = altura #passando minha altura pra váriavel
        self.area = 0  # iniciando minha area sem valor
        self.perimetro = 0  # iniciando minha area sem valor


    def calcularAreareta(self): # função para calcular a area
        self.area = self.la1 * self.la2 # manipulando e calculando meus valores passando para a area
        return self.area #retornando a area para a classe de execução assim que a função é chamada

    def calculaPerimetroreta(self): # função para calcular o perimetro
        self.perimetro = 2 * (self.la1 + self.la2) # manipulando e calculando meus valores passando para o perimetro
        return self.perimetro #retornando o perimetro para a classe de execução assim que a função é chamada
