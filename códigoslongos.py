from circulo import Circulo  # importando a classe circulo
from retangulo import Retangulo  # importando a classe retangulo

print("Programa para calcular formas geométricas") # Nome do Programa

print("BEM VINDO!!!\nVAMOS APRENDER GEOMETRIA")  # boas vindas

def retanguloarea(): #defindo a função
    print("Voce escolheu a area do Retangulo.") # Situando o usuário
    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        base = float(input("Digite a base do retangulo: "))  # recebndo os valores e setando nas variaveis
        altura = float(input("Digite a altura do retangulo: "))
        meuRetangulo = Retangulo(base, altura) #instanciando a minha classe e enviando meus parametros
        areareta = meuRetangulo.calcularAreareta() #chamando a classe para receber o resultado
        print("\nA area do retangulo é {:.2f} cm²".format(areareta))  # apresentando a area do circulo para o usuario
        escolha()# chamando a função novamente
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!"
            "\nPor Favor, tente novamente.")  # utilizando barra invertida e n quebramos linha
        escolha()  # chamando a função novamente

def retanguloperi():  #definindo a função
    print("Voce escolheu o Perimetro do Retangulo.")  #Situando o usuário
    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        base = float(input("Digite a base do retangulo: ")) #recebendo os valores e setando nas variaveis
        altura = float(input("Digite a altura do retangulo: "))
        meuRetangulo = Retangulo(base, altura)  #instanciando a classe e passando os parametros
        meuperi = meuRetangulo.calculaPerimetroreta() # #chamando a classe para receber o resultado
        print("\nO perimetro do retangulo é {:.2f} cm".format(meuperi))  # apresentando a area do circulo para o usuario
        escolha()# chamando a função novamente
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!"
            "\nPor Favor, tente novamente.")  # utilizando barra invertida e n quebramos linha
        escolha()  # chamando a função novamente

def circuloarea():  #definindo a função
    print("Voce escolheu a Area do circulo.")  # situando o usuario
    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        numraio = float(input("Digite o raio: "))  # recebendo os parametros do usuario e setando nas variaveis
        meuCirculo = Circulo(numraio)  # instaciando a classe
        minhaarea = meuCirculo.calcularAreacirc()  # recebendo a area da classe circulo
        print("\nA area do círculo é {:.2f} cm".format(minhaarea))  # apresentando a area do circulo para o usuario
        escolha()# chamando a função novamente
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!"
            "\nPor Favor, tente novamente.")  # utilizando barra invertida e n quebramos linha
        escolha()  # chamando a função novamente

def circuloperi():  #definindo a função
    print("Voce escolheu o Perimetro do circulo.")  #situando o usuario
    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        numraio = float(input("Digite o raio: "))  # recebendo os parametros do usuario
        meuCirculo = Circulo(numraio)  # instaciando a classe
        meuperimetro = meuCirculo.calculaPerimetrocirc()  # recebendo o perimetro da classe circulo
        print("\nO Perimetro do Círculo é {:.2f} cm ".format(meuperimetro))  # apresentando o perimetro do circulo para o usuario
        escolha() # chamando a função novamente
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!\nPor Favor, tente novamente.")  # utilizando barra invertida e n quebramos linha
        escolha()  # chamando a função novamente

def escolha():#definindo a função
    print("\nEscolha a operação desejada:\n( 1 ) Calcular a Area do Retangulo.\n( 2 ) Calcular o Perimetro do Retangulo."
          "\n( 3 ) Calcular a Area do Circulo.\n( 4 ) Calcular o Perimetro do Circulo.\n( 5 ) Finalizar.") #menu de opções
    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        op = int(input("Opção: "))  #armazenando a escolha na variavel op
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!"
            "\nPor Favor, tente novamente.")  # utilizando barra invertida e n quebramos linha
        escolha()  # chamando a função novamente, para uma correção dos valores ou sair do programa.
    try:  # utilizamos o try para tratar teclas que não sejam numéricas com excessão do ponto para valores flutuantes
        if op == 1:
            retanguloarea()   # chamada de função
        elif op == 2:
           retanguloperi()    # chamada de função
        elif op == 3:     #tratando e direcionando o programa conforme escolha
            circuloarea()
        elif op == 4:  # tratando e direcionando o programa conforme escolha
            circuloperi()
        elif op == 5:  # tratando e direcionando o programa conforme escolha
            print('ATÉ LOGO !')
            exit()  # opção para sair do programa
        else: #caso escolha fora do escopo
            print("Opção inválida, a escolha deve ser uma operação da lista!\nPor Favor, tente novamente.")
            escolha()#chamada de função
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, virgula ou deixe vazio!\nA entrada deve ser primeiro um número seguido ou não de ponto!"
            "\nPor Favor, tente novamente.")  # utilizando barra invertida e n quebramos linha
        escolha()  # chamando a função novamente, para uma correção dos valores ou sair do programa.
escolha() #inicializando o programa


#fim do programa

