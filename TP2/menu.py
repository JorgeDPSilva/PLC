import os
import tp1_yacc as yacc

def menu():
    print(" ______________________________________________MENU", end= "")
    print("__________________________________________________")
    print("|                                                    ", end = "")
    print("                                                |")
    print("|\t[1] - Ler 4 números e verificar se podem ", end = "")
    print("ser uma quadrado ou não.                            |")
    print("|\t[2] - Ler um inteiro N e depois ler ", end = "")
    print("N inteiros e imprimir o menor.                           |")
    print("|\t[3] - Ler N numeros e imprimir o seu produtório.", end = "")
    print("                                             |")
    print("|\t[4] - Contar e imprimir os numeros impares ", end = "")
    print("de uma sequencia de numeros naturais.", end = "")
    print("             |")
    print("|\t[5] - Ler e armazenar N numeros num array.", end = "")
    print(" Imprimir por ordem inversa.", end = "")
    print("                       |")
    print("|\t[6] - Invocar uma funcao potencia() que le do input", end = "")
    print(" a base e o expoente e calcula a potencia.|")
    print("|\t[0] - Sair.                                       ", end = "")
    print("                                           |")
    print("|                                                   ", end = "")
    print("                                                 |")
    print("|_____________________________________________________", end = "")
    print("_______________________________________________|")
    print("")

def init():

    menu()
    opcao = input("Escolha uma opcao:")
    while(opcao != 0):
        
        if opcao == '1':

            yacc.parser.file = open("vmFiles/ex1.vm", "w")
            with open('funcFiles/ex1.txt', 'r') as file:
                program = file.read().rstrip()
            yacc.parser.parse(program)
            opcao = 0

        elif opcao == '2':

            yacc.parser.file = open("vmFiles/ex2.vm", "w")
            with open('funcFiles/ex2.txt', 'r') as file:
                program = file.read().rstrip()
            yacc.parser.parse(program)
            opcao = 0

        elif opcao == '3':

            yacc.parser.file = open("vmFiles/ex3.vm", "w")
            with open('funcFiles/ex3.txt', 'r') as file:
                program = file.read().rstrip()
            yacc.parser.parse(program)
            opcao = 0
            
        elif opcao == '4':
            yacc.parser.file = open("vmFiles/ex4.vm", "w")
            with open('funcFiles/ex4.txt', 'r') as file:
                program = file.read().rstrip()
            yacc.parser.parse(program)
            opcao = 0

        elif opcao == '5':
            yacc.parser.file = open("vmFiles/ex5.vm", "w")
            with open('funcFiles/ex5.txt', 'r') as file:
                program = file.read().rstrip()
            yacc.parser.parse(program)
            opcao = 0
        elif opcao == '6':
            yacc.parser.file = open("vmFiles/ex6.vm", "w")
            with open('funcFiles/ex6.txt', 'r') as file:
                program = file.read().rstrip()
            yacc.parser.parse(program)
            opcao = 0
        elif opcao == '0':
            print("Programa terminado.\n")
            os.system("rm vmFiles/*")
            opcao = 0
        else:
            print("Valor invalido")
            opcao = input("Escolha uma opcao:")
init()


    

