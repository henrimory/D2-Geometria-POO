from circulo import Circulo  # importando a classe circulo
from retangulo import Retangulo  # importando a classe retangulo
from triangulo import Triangulo # importando a classe triangulo
from trapezio import Trapezio # importando a classe Trapezio


print("Programa para calcular formas geométricas") # Nome do Programa

print("BEM VINDO!!!\nVAMOS APRENDER GEOMETRIA")  # boas vindas

print("Escolha qual a forma deseja calcular!") # orientação ao usuário

def escolha():
    forma = input("1 - Circulo\n2 - Retangulo\n3 - Triangulo\n4 - Trapézio\n5 - Sair\n-->")  # menu de opções

    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        if forma == "1":
            raio = float(input("Quantos centimetros tem o raio:"))
            meuCirculo = Circulo(raio)  # instaciando a classe
            minhaarea = meuCirculo.calcularAreacirc()  # recebendo a area da classe circulo
            meuperimetro = meuCirculo.calculaPerimetrocirc()  # recebendo o perimetro da classe circulo
            print("\nA area do círculo é {:.2f} cm".format(minhaarea))
            print("\nO Perimetro do Círculo é {:.2f} cm ".format(meuperimetro))
        elif forma == "2":
            base = float(input("Digite a base do retangulo: "))  # recebndo os valores e setando nas variaveis
            altura = float(input("Digite a altura do retangulo: "))
            meuRetangulo = Retangulo(base, altura)  # instanciando a minha classe e enviando meus parametros
            areareta = meuRetangulo.calcularAreareta()  # chamando a classe para receber o resultado
            meuperi = meuRetangulo.calculaPerimetroreta()  # #chamando a classe para receber o resultado
            print("\nA area do retangulo é {:.2f} cm²".format(areareta))  # apresentando a area do circulo para o usuario
            print("\nO perimetro do retangulo é {:.2f} cm".format(meuperi))  # apresentando a area do circulo para o usuario
        elif forma == "3":
            lado1 = float(input("Digite o lado 1 do triangulo: "))  # recebndo os valores e setando nas variaveis
            lado2 = float(input("Digite o laodo 2 do triangulo: "))
            base = float(input("Digite a base do triangulo: "))  # recebndo os valores e setando nas variaveis
            altura = float(input("Digite a altura do triangulo: "))
            meuTriangulo = Triangulo(lado1, lado2, base, altura)  # instanciando a minha classe e enviando meus parametros
            areatri = meuTriangulo.calcularAreaTri()  # chamando a classe para receber o resultado
            peritri = meuTriangulo.calculaPerimetroTri()  # #chamando a classe para receber o resultado
            print("\nA area do triangulo é {:.2f} cm²".format(areatri))  # apresentando a area do circulo para o usuario
            print("\nO perimetro do triangolo é {:.2f} cm".format(peritri))  # apresentando a area do circulo para o usuario
        elif forma == "4":
            lado1 = float(input("Digite o lado 1 do trapezio: "))  # recebndo os valores e setando nas variaveis
            lado2 = float(input("Digite o laodo 2 do trapezio: "))
            basemenor = float(input("Digite a base Menor do trapezio: "))  # recebndo os valores e setando nas variaveis
            basemaior = float(input("Digite a base Maior do trapezio: "))  # recebndo os valores e setando nas variaveis
            altura = float(input("Digite a altura do trapezio: "))
            meuTrapezio = Trapezio(lado1, lado2, basemenor, basemaior, altura)  # instanciando a minha classe e enviando meus parametros
            areatrap = meuTrapezio.calcularAreaTrap()  # chamando a classe para receber o resultado
            peritrap = meuTrapezio.calculaPerimetroTrap()  # #chamando a classe para receber o resultado
            print("\nA area do trapezio é {:.2f} cm²".format(areatrap))  # apresentando a area do circulo para o usuario
            print("\nO perimetro do trapezio é {:.2f} cm".format(peritrap))  # apresentando a area do circulo para o usuario
        elif forma == "5":
            print("ATÉ A PRÓXIMA!!!")  # despedida
            exit()  #finaliza o programa
        else:
            print("Opção inválida, a escolha deve ser uma operação da lista!\nPor Favor, tente novamente.")  # caso usuário digite tecla que não faz parte das opções
            escolha()   # chamada da função para reinicialização do programa
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!\nPor Favor, tente novamente.")
        escolha()  # chamada da função para reinicialização do programa
escolha() # chamada da função para inicialização do programa
