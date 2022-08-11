#Arthur Neumann Salerno 

#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
#operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas 
#seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da 
#operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e 
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. 

def tira_espaco(string):
    return string.replace(" ", "")


def separa(string, delimiter):
    array = []
    to_add = ""
    for i in range(0, len(string)):
        if (not string[i] == delimiter):
            to_add += str(string[i])
            if i == len(string) - 1:
                array.append(to_add)
        else:
            array.append(to_add)
            to_add = ""
    return array


def uniao(conj1, conj2):
    array = []
    array.extend(conj1)
    array.extend(conj2)

    for i in range(len(array)-1, 0, -1):
        if array.count(array[i]) > 1:
            array.pop(i)
    return array


def intersecao(conj1, conj2):
    array = []
    for i in conj1:
        for j in conj2:
            if i == j and i not in array:
                array.append(i)
    return array


def diferenca(conj1, conj2):
    array = []
    array.extend(conj1)
    for i in conj1:
        for j in conj2:
            if i == j:
                array.remove(i)
    return array


def prod_cartesiano(conj1, conj2):
    array = []
    for i in conj1:
        for j in conj2:
            array.append("(%s, %s)" % (i, j))
    return array


f = open('teste3.txt', 'r')

num_op = f.readline()

for i in range(0, int(num_op)):
    optype = f.readline().strip()
    set1 = f.readline().strip()
    set2 = f.readline().strip()

    _set1 = separa(tira_espaco(set1), ',')
    _set2 = separa(tira_espaco(set2), ',')

    if optype == 'U':
        conj_1 = ", ".join(_set1)
        conj_2 = ", ".join(_set2)
        resposta = ", ".join(uniao(_set1, _set2))
        print("União: ", "conjunto 1: {%s} conjunto 2: {%s} Resultado: {%s}" % (conj_1, conj_2, resposta))

    if optype == 'I':
        conj_1 = ", ".join(_set1)
        conj_2 = ", ".join(_set2)
        resposta = ", ".join(intersecao(_set1, _set2))
        print("Interseção: ", "conjunto 1: {%s} conjunto 2: {%s} Resultado: {%s}" % (conj_1, conj_2, resposta))

    if optype == 'D':
        conj_1 = ", ".join(_set1)
        conj_2 = ", ".join(_set2)
        resposta = ", ".join(diferenca(_set1, _set2))
        print("Diferença: ", "conjunto 1: {%s} conjunto 2: {%s} Resultado: {%s}" % (conj_1, conj_2, resposta))

    if optype == 'C':
        conj_1 = ", ".join(_set1)
        conj_2 = ", ".join(_set2)
        resposta = ", ".join(prod_cartesiano(_set1, _set2))
        print("Produto Cartesiano: ", "conjunto 1: {%s} conjunto 2: {%s} Resultado: {%s}" % (conj_1, conj_2, resposta))
