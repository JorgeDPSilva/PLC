import json

def genericHtml(headers,info,file):
    
    f = open("html/" + file, "w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

    f.write("<style>\n")
    f.write("\ttable,td,th {\n \t\tborder: 1px solid black; \n")
    f.write("\t\tborder-collapse: collapse;\n \t\ttext-align: center;\n \t}\n")
    f.write("</style>\n")

    f.write("\t<table>\n")
    f.write("\t\t<tr>\n")
    # headers
    for i in range(0,len(headers)):
        f.write("\t\t\t<th>")
        f.write(headers[i])
        f.write("</th>\n")
    f.write("\t\t</tr>\n")

    for key,value in info.items():
        f.write("\t\t<tr>\n")
        f.write("\t\t\t<td>")
        f.write(key)
        f.write("</td>\n")
        f.write("\t\t\t<td>")
        f.write(str(value))
        f.write("</td>\n")
        f.write("\t\t</tr>\n")
    
    f.write("\t</table>\n")
    f.write("</html>")
    f.close()

# aceita listas nos values do dicionario info
def genericHtmlList(headers,info,file):
    f = open("html/" + file, "w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

    f.write("<style>\n")
    f.write("\ttable,td,th {\n \t\tborder: 1px solid black; \n")
    f.write("\t\tborder-collapse: collapse;\n \t\ttext-align: center;\n \t}\n")
    f.write("</style>\n")

    f.write("\t<table>\n")
    f.write("\t\t<tr>\n")
    # headers
    for i in range(0,len(headers)):
        f.write("\t\t\t<th>")
        f.write(headers[i])
        f.write("</th>\n")
    f.write("\t\t</tr>\n")

    for key,value in info.items():
        f.write("\t\t<tr>\n")
        f.write("\t\t\t<td>")
        f.write(key)
        f.write("</td>\n")
        f.write("\t\t\t<td>\n")
        for i in value:
            f.write("\t\t\t\t")
            f.write(i)
            f.write("<br>\n")
        f.write("\t\t\t</td>\n")
        f.write("\t\t</tr>\n")
    
    f.write("\t</table>\n")
    f.write("</html>")
    f.close()

def ex1ToHtml(info):

    dic = {}
    
    for key,value in info.items():
        dic[value[0]] = value[1]
    
    dic = dict(sorted(dic.items(), key=lambda item: item[0]))
    genericHtml(["Nome", "Entidade"], dic, "ex1.html")


def ex2ToHtml(info):

    dic = {}
    for value in info.values():
        if value[1] not in dic:
            dic[value[1]] = 1
        else:   
            dic[value[1]] += 1
    dic = dict(sorted(dic.items(), key = lambda item: item[0]))

    genericHtml(["Entidade", "Quantidade"],dic,"ex2.html")

def ex3toHtml(info):
     
    dic = {}
    for key,value in info.items():
        if value[2] not in dic.keys():
            dic[value[2]] = []
            dic[value[2]].append(value[0])
        else:
            dic[value[2]].append(value[0])

    dic = dict(sorted(dic.items(), key = lambda item: item[0]))

    genericHtmlList(["Nível","Utilizadores"], dic, "ex3.html")

def ex4toHtml(info):
    dic = {}
    
    for key,value in info.items():
        if value[1] not in dic.keys():
            dic[value[1]] = []
            dic[value[1]].append(value[0])
        else:
            dic[value[1]].append(value[0])

    for key in dic.keys():
        dic[key] = sorted(dic[key], key=str.lower)

    dic = dict(sorted(dic.items(), key = lambda item: item[0]))

    genericHtmlList(["Entidade", "Nome"], dic, "ex4.html")

def ex5toHtml(info):
    dic_ent = {}
    dic_niv = {}

    for key,value in info.items():
        if value[2] not in dic_niv:
            dic_niv[value[2]] = 1
        else:
            dic_niv[value[2]] += 1

        if value[1] not in dic_ent:
            dic_ent[value[1]] = 1
        else:
            dic_ent[value[1]] += 1
    
    dic_ent = dict(sorted(dic_ent.items(), key = lambda item: item[1], reverse=True))
    
    f = open("html/ex5.html","w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

    f.write("<style>\n")
    f.write("\ttable,td,th {\n \t\tborder: 1px solid black; \n")
    f.write("\t\tborder-collapse: collapse;\n \t\ttext-align: center;\n")
    f.write("\t\tmargin-right: 30px;\n\t}\n")
    f.write("\t.table-2{\n \t\theight:50%;\n\t}\n")
    f.write("\tdiv {\n \t\tdisplay: flex;\n\t}\n")
    f.write("\tspan {\n \t\tfont-weight: bold;\n\t}\n")
    f.write("\tspan {\n \t\tfont-weight: bold;\n\t}\n")
    f.write("</style>\n")

    f.write("<p>")
    f.write("<span>")
    f.write("Total de utilizadores: ")
    f.write("</span>")
    f.write(str(len(info.keys())))
    f.write("</p>\n")

    f.write("<p>")
    f.write("<span>")
    f.write("Total de entidades: ")
    f.write("</span>")
    f.write(str(len(dic_ent.keys())))
    f.write("</p>\n")
    f.write("<div>\n")
    f.write("\t<table>\n")
    f.write("\t\t<tr>\n")

    # headers
    f.write("\t\t\t<th>")
    f.write("Entidade")
    f.write("</th>\n")
    f.write("\t\t\t<th>")
    f.write("Quantidade")
    f.write("</th>\n")

    for key,value in dic_ent.items():
        f.write("\t\t<tr>\n")
        f.write("\t\t\t<td>")
        f.write(key)
        f.write("</td>\n")
        f.write("\t\t\t<td>")
        f.write(str(value))
        f.write("</td>\n")
        f.write("\t\t</tr>\n")

    
    f.write("\t</table>\n")

    f.write("\t<table class = \"table-2\">\n")
    f.write("\t\t<tr>\n")

    # headers
    f.write("\t\t\t<th>")
    f.write("Nível")
    f.write("</th>\n")
    f.write("\t\t\t<th>")
    f.write("Quantidade")
    f.write("</th>\n")

    for key,value in dic_niv.items():
        f.write("\t\t<tr>\n")
        f.write("\t\t\t<td>")
        f.write(key)
        f.write("</td>\n")
        f.write("\t\t\t<td>")
        f.write(str(value))
        f.write("</td>\n")
        f.write("\t\t</tr>\n")

    f.write("\t</table>\n")
    f.write("</div>\n")

    f.write("</html>")
    f.close()

def ex6toHtml(info):
    lista=["Nome","Mail","Entidade","Nível","Chamadas backend"]
    info = dict(sorted(info.items(), key = lambda item:item[1]))

    f = open("html/ex6.html","w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

    f.write("<style>\n")
    f.write("\ttable,td,th {\n \t\tborder: 1px solid black; \n") 
    f.write("\t\tborder-collapse: collapse;\n \t\ttext-align: center;\n")
    f.write("\t\tmargin-right: 30px;\n\t}\n")
    f.write("</style>\n")

    f.write("\t<table>\n")
    f.write("\t\t<tr>\n") #uma linha da tabela
    for i in lista:
        f.write("\t\t\t<th>")
        f.write(i)
        f.write("</th>\n")
    f.write("\t\t</tr>\n")
    for key,value in info.items():
        f.write("\t\t<tr>\n")
        f.write("\t\t\t<td>")
        f.write(value[0])
        f.write("</td>\n")
        f.write("\t\t\t<td>")
        f.write(key)
        f.write("</td>\n")
        for i in range(1,len(value)):
            f.write("\t\t\t<td>")
            f.write(value[i])
            f.write("</td>\n")
        f.write("\t\t</tr>\n")
    f.write("\t</table>\n")    
    f.write("</html>")
    f.close()


def toJson(info):
    reg = []
    counter = 0

    j = open('json/data.json', 'w+', encoding='utf-8')

    for key,value in info.items():
        l=[]
        l.append(key)
        for i in value:
            l.append(i)
        reg.append(l)
        
        counter+=1
        if counter == 20:
            break
    
    json.dump(reg, j, ensure_ascii=False, indent=4)
    j.close()