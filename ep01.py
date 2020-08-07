# coding=utf-8
def main():
    # Pergunta ao usuário o modo
    modoOpera = int(input("modo:"))

    # Executa o modo de operação 1
    if modoOpera == 1 :

        # Pede para o usuário escolher os numeros que terao os quadrados somados
        resto = contador = mult = n1 = n2 = n3 = n4 = n = 0
        n1 = int(input("\n n1: "))
        n2 = int(input("\n n2: "))
        n3 = int(input("\n n3: "))
        n4 = int(input("\n n4: "))

        # Numero que sera igual a soma dos quadrados anteriores
        n = int(input("n: \n"))

        # Testa se a variável n é igual a soma dos quadrados
        quadrado = n1 * n1 + n2 * n2 + n3 * n3 + n4 * n4
        if n == quadrado :
            print("Verdadeiro")
        else :
            print("Falso")

    #parte 2 do exercicio+
    else:
        n = int(input("\nn:"))

        #variavel para testar se o numero deu certo
        primo = testador = False

        n1 = 2
        n2 = 3
        n3 = 5
        n4 = 7
        aux = 9

        while testador == False :
            primo = False
            #verifica se a soma dos quadrados e igual a n
            if n1**2 + n2**2 + n3**2 + n4**2 == n:
               testador = True
               print("\n",int(n1)," ", int(n2)," ", int(n3),
                         " ", int(n4))
            elif (n1**2 + n2**2 + n3**2 + n4**2) > n:
               testador = True
               print("Falso")
            else:
                while primo == False:
                    div = 0
                    i = 2
                    while i <= int(aux/2):
                        if aux % i == 0:
                            div += 1
                            aux += 2
                        i += 1
                    if div == 0:
                        primo = True
                        n1 = n2
                        n2 = n3
                        n3 = n4
                        n4 = aux
                        aux += 2

main()
