import re, func, os

def printMenu():
    
    print("\n \t\t\t\t\tMenu\n")
    print("\t[1] - Produz uma listagem apenas com o nome e a ", end = "") 
    print("entidade do utilizador.")
    print("\t[2] - Produz uma lista das entidades referenciadas,", end = "")
    print(" com o número de utilizadores.")
    print("\t[3] - Distribuição de utilizadores por níveis de acesso.")
    print("\t[4] - Listagem dos utilizadores, agrupados por entidade.")
    print("\t[5] - Indicadores:\n \t\t-> Quantos utilizadores?\n",end = "") 
    print("\t\t-> Quantas entidades?\n", end="")
    print("\t\t-> Qual a distribuição em número por entidade?\n",end="")
    print("\t\t-> Qual a distribuição em número por nível?")
    print("\t[6] - Imprimir toda a informação.")
    print("\t[7] - Imprimir os 20 primeiros registos num novo ficheiro", end="")
    print(" de output em formato Json.")
    print("\t[0] - Sair")


def init():

    printMenu()
    val = input("Escolha uma opção:")
    f = open("clav-users.txt", "r")
    info = {}

    for line in f:
        string = re.sub(r"\n",r"",line)
        l = re.split(r'::',string)
        info[l[1]] = [l[0]] + l[2:]

    while val != 0:

        if val == '1':
            # Produz uma listagem apenas com o nome e a entidade do utilizador, 
            # ordenada alfabeticamente por nome
            func.ex1ToHtml(info)
            print("Ficheiro html criado.")
            os.system("open -a \"Google Chrome\" html/ex1.html")

        elif val == '2':
            # Produz uma lista ordenada alfabeticamente das entidades referenciadas, 
            # indicando, para cada uma, quantos utilizadores estão registados;
            func.ex2ToHtml(info)
            print("Ficheiro html criado.")
            os.system("open -a \"Google Chrome\" html/ex2.html")

        elif val == '3':
            # Qual a distribuição de utilizadores por níveis de acesso?
            func.ex3toHtml(info)
            print("Ficheiro html criado.")
            os.system("open -a \"Google Chrome\" html/ex3.html")

        elif val == '4':
            # Produz uma listagem dos utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta
            # pelo nome
            func.ex4toHtml(info)
            print("Ficheiro html criado.")
            os.system("open -a \"Google Chrome\" html/ex4.html")

        elif val == '5':
            #Indicadores
            func.ex5toHtml(info)
            print("Ficheiro html criado.")
            os.system("open -a \"Google Chrome\" html/ex5.html")

        elif val == '6':
            #imprimir toda a informação
            func.ex6toHtml(info)
            print("Ficheiro html criado.")
            os.system("open -a \"Google Chrome\" html/ex6.html")
        elif val == '7':
            # imprimir os 20 primeiros registos num novo ficheiro de output mas em formato Json
            func.toJson(info)
            print("Ficheiro json criado.")
            os.system("open json/data.json")
        elif val == '0':
            print("Finalizado")
            os.system("rm html/* json/data.json")
            break
        else:
            print("Valor inválido.")
        print()
        printMenu()
        val = input("Escolha uma opção:")

    f.close()

init()