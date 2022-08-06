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

    for i in range(len(array)-1, 0):
        if array.count(i) > 1:
            array.remove(i)
    return array


def intersecao(conj1, conj2):
    array = []
    for i in conj1:
        for j in conj2:
            if i == j:
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


f = open('texto.txt', 'r')

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
