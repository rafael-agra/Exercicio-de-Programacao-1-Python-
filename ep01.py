# coding=utf-8
"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Rafael Agra de Castro Motta
  NUSP : 11807192
  Turma: 7
  Prof.: André Fujita

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

	[Seu programa]

  """

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
