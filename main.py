import queue

grafo = {}


def grauDoVertice(vertice):
    if vertice not in grafo:
        return -1
    if type(grafo[vertice]) is dict:  # grafo valorado
        grau_entrada = sum(grafo[v][vertice] for v in grafo if vertice in grafo[v])
        grau_saida = sum(grafo[vertice][v] for v in grafo[vertice])
        return grau_entrada + grau_saida
    else:  # grafo não valorado
        return len(grafo[vertice])


def verificaAdjacencia(vertice1, vertice2):
    if vertice2 in grafo[vertice1]:
        print(f"{vertice1} é adjacente a {vertice2}")
    else:
        print(f"{vertice1} não é adjacente a {vertice2}")


def raioDiametro():
    n = len(grafo)
    diametro = float('inf')
    for i in range(n):
        dist = [-1] * n
        dist[i] = 0
        fila = queue.Queue()
        fila.put(i)
        while not fila.empty():
            v = fila.get()
            for w in grafo[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    fila.put(w)
        raio = min(dist)
        diametro = min(diametro, max(dist))
    print("\nO raio do grafo é : "+ str(raio))
    print("\nO diâmetro do grafo é: "+ str(diametro))


def listaDeAdjacencia():
    for i in grafo.keys():
        print(str(i) + " -> " + str(grafo[i]))


def ordemTamanho ():

    print("\nA ordem do grafo é: " + str(len(grafo)))
    print("\nO tamanho do grafo é: " + str(sum(len(v) for v in grafo.values()) // 2))


def visualizar (valorado):

    if valorado == 1:
        for i in grafo.keys():
            print(str(i) + " -> " + str(grafo[i]))
    elif valorado == 2:
        for i in grafo.keys():
            print(str(i) + " -> " + str(grafo[i][0]))


def addVerticeNaoValoradoNaoDirecionado ():

    verticeOrigem, verticeDestino = input("Digite o vertice inicial | vertice final: ").split()
    if (verticeDestino) not in grafo[(verticeOrigem)]:
        grafo[(verticeOrigem)].append((verticeDestino))
    if (verticeOrigem) not in grafo[(verticeDestino)]:
        grafo[(verticeDestino)].append((verticeOrigem))


def addVerticeNaoValoradoDirecionado ():

    verticeOrigem, verticeDestino = input("Digite o vertice inicial | vertice final: ").split()
    if (verticeDestino) not in grafo[(verticeOrigem)]:
        grafo[(verticeOrigem)].append((verticeDestino))


def addVerticeValoradoNaoDirecionado ():

    verticeOrigem, verticeDestino, valor = input("Digite o vertice inicial | vertice final | valor: ").split()
    if (verticeDestino) not in grafo[(verticeOrigem)]:
        grafo[(verticeOrigem)].append(((verticeDestino), int(valor)))
    if (verticeOrigem) not in grafo[int(verticeDestino)]:
        grafo[(verticeDestino)].append(((verticeOrigem), int(valor)))


def addVerticeValoradoDirecionado ():

    verticeOrigem, verticeDestino, valor = input("Digite o vertice inicial | vertice final | valor: ").split()
    grafo[(verticeOrigem)].append(((verticeDestino), (valor)))


def adicionarNovoVertice ():

    grafo[input("Digite o nome do vértice: ")] = []


def adicionarNovaAresta (userOption):
    match userOption:
        case 1:
            addVerticeValoradoDirecionado()
        case 2:
            addVerticeValoradoNaoDirecionado()
        case 3:
            addVerticeNaoValoradoDirecionado()
        case 4:
            addVerticeNaoValoradoNaoDirecionado()


def criarNaoValoradoNaoDirecionadoArquivo():

    arquivo = open(input("") + ".txt", "r", encoding="utf8")
    linhasArquivo = [line.strip() for line in arquivo.readlines()]

    numeroVertices = linhasArquivo[0]
    nomes = linhasArquivo[1].split()
    arestas = linhasArquivo[2:]

    for i in range(int(numeroVertices)):
        grafo[nomes[i]] = []

    for i in arestas:
        if (i[-1]) not in grafo[(i[0])]:
            grafo[(i[0])].append((i[-1]))
        if (i[0]) not in grafo[(i[-1])]:
            grafo[(i[-1])].append((i[0]))


def criarNaoValoradoNaoDirecionadoInput():

    numeroVertices = int(input("Digite o número de vértices: "))
    numeroArestas = int(input("Digite o número de arestas: "))

    for i in range(numeroVertices):
        grafo[input("Digite o nome do vértice: ")] = []

    for i in range(numeroArestas):
        verticeOrigem, verticeDestino = input("Digite o vertice inicial | vertice final: ").split()
        if (verticeDestino) not in grafo[(verticeOrigem)]:
            grafo[(verticeOrigem)].append((verticeDestino))
        if (verticeOrigem) not in grafo[(verticeDestino)]:
            grafo[(verticeDestino)].append((verticeOrigem))


def naoValoradoNaoDirecionado(tipoUso):

    match tipoUso:
        case 1:
            criarNaoValoradoNaoDirecionadoInput()
        case 2:
            criarNaoValoradoNaoDirecionadoArquivo()


def criarNaoValoradoDirecionadoArquivo():

    arquivo = open(input("") + ".txt", "r", encoding="utf8")
    linhasArquivo = [line.strip() for line in arquivo.readlines()]

    numeroVertices = linhasArquivo[0]
    nomes = linhasArquivo[1].split()
    arestas = linhasArquivo[2:]

    for i in range(int(numeroVertices)):
        grafo[nomes[i]] = []

    for i in arestas:
        if (i[-1]) not in grafo[(i[0])]:
            grafo[(i[0])].append((i[-1]))


def criarNaoValoradoDirecionadoInput():

    numeroVertices = int(input("Digite o número de vértices: "))
    numeroArestas = int(input("Digite o número de arestas: "))

    for i in range(numeroVertices):
        grafo[input("Digite o nome do vértice: ")] = []

    for i in range(numeroArestas):
        verticeOrigem, verticeDestino = input("Digite o vertice inicial | vertice final: ").split()
        if (verticeDestino) not in grafo[(verticeOrigem)]:
            grafo[(verticeOrigem)].append((verticeDestino))


def naoValoradoDirecionado(tipoUso):

    match tipoUso:
        case 1:
            criarNaoValoradoDirecionadoInput()
        case 2:
            criarNaoValoradoDirecionadoArquivo()


def criarValoradoNaoDirecionadoArquivo():

    arquivo = open(input("") + ".txt", "r", encoding="utf8")
    linhasArquivo = [line.strip() for line in arquivo.readlines()]

    numeroVertices = linhasArquivo[0]
    nomes = linhasArquivo[1].split()
    arestas = linhasArquivo[2:]

    for i in range(int(numeroVertices)):
        grafo[nomes[i]] = []

    for i in arestas:
        if ((i[-1])) not in grafo[(i[0])]:
            grafo[(i[0])].append(((i[1]), (i[-1])))
        if ((i[0])) not in grafo[(i[-1])]:
            grafo[(i[1])].append(((i[0]), (i[-1])))


def criarValoradoNaoDirecionadoInput():

    numeroVertices = int(input("Digite o número de vértices: "))
    numeroArestas = int(input("Digite o número de arestas: "))

    for i in range(numeroVertices):
        grafo[input("Digite o nome do vértice: ")] = []

    for i in range(numeroArestas):
        verticeOrigem, verticeDestino, valor = input("Digite o vertice inicial | vertice final | valor: ").split()
        if (verticeDestino) not in grafo[(verticeOrigem)]:
            grafo[(verticeOrigem)].append(((verticeDestino), int(valor)))
        if (verticeOrigem) not in grafo[int(verticeDestino)]:
            grafo[(verticeDestino)].append(((verticeOrigem), int(valor)))


def valoradoNaoDirecionado(tipoUso):

    match tipoUso:
        case 1:
            criarValoradoNaoDirecionadoInput()
        case 2:
            criarValoradoNaoDirecionadoArquivo()


def criarValoradoDirecionadoArquivo ():

    arquivo = open(input("") + ".txt", "r", encoding="utf8")
    linhasArquivo = [line.strip() for line in arquivo.readlines()]

    numeroVertices = linhasArquivo[0]
    nomes = linhasArquivo[1].split()
    arestas = linhasArquivo[2:]

    for i in range(int(numeroVertices)):
        grafo[nomes[i]] = []

    for i in arestas:
        grafo[(i[0])].append(((i[1]), (i[-1])))


def criarValoradoDirecionadoInput ():

    numeroVertices = int(input("Digite o número de vértices: "))
    numeroArestas = int(input("Digite o número de arestas: "))

    for i in range(numeroVertices):
        grafo[input("Digite o nome do vértice: ")] = []

    for i in range(numeroArestas):
        verticeOrigem, verticeDestino, valor = input("Digite o vertice inicial | vertice final | valor: ").split()
        grafo[(verticeOrigem)].append(((verticeDestino), (valor)))


def valoradoDirecionado (tipoUso):

    match tipoUso:
        case 1:
            criarValoradoDirecionadoInput()
        case 2:
            criarValoradoDirecionadoArquivo()


def criarGrafo (userOption):

    tipoUso = int(input("1 - ESCREVER\n"
                        "2 - ARQUIVO\n"
                        "valor: "))

    match userOption:
        case 1:
            valoradoDirecionado(tipoUso)
        case 2:
            valoradoNaoDirecionado(tipoUso)
        case 3:
            naoValoradoDirecionado(tipoUso)
        case 4:
            naoValoradoNaoDirecionado(tipoUso)


def checkOption (valorado, direcionado):

    option = 0

    match valorado:
        case 1:
            match direcionado:
                case 1:
                    option = 1
                case 2:
                    option = 2
        case 2:
            match direcionado:
                case 1:
                    option = 3
                case 2:
                    option = 4

    return option


def menu (opcao, valorado, direcionado):

    while(1):
        opcaoMenu = int(input("1 - ADICIONAR NOVO VERTICE\n"
                          "2 - ADICIONAR NOVA ARESTA\n"
                          "3 - VISUALIZAR GRAFO\n"
                          "4 - ORDEM E TAMANHO\n"
                          "5 - LISTA DE VERTICES ADJACENTES\n"
                          "6 - GRAU DE UM VERTICE\n"
                          "7 - VERIFICAR SE DOIS VERTICES SÁO ADJACENTES OU NÃO\n"
                          "8 - RAIO E DIAMETRO\n"
                          "0 - SAIR\n"))

        match opcaoMenu:
            case 0:
                exit(0)
            case 1:
                adicionarNovoVertice()
            case 2:
                adicionarNovaAresta(opcao)
            case 3:
                visualizar(valorado)
            case 4:
                ordemTamanho()
            case 5:
                vertice = int(input("\nESCREVA O VERTICE QUE DESEJA SER CHECADO: "))
                listaDeAdjacencia(opcao, vertice)
            case 6:
                vertice = int(input("\nESCREVA O VERTICE QUE DESEJA SER CHECADO: "))
                grauDoVertice(vertice)
            case 7:
                vertice1, vertice2 = int(input("\nESCREVA OS VERTICES QUE VOCÊ DESEJA CHECAR: "))
                verificaAdjacencia(vertice1, vertice2)
            case 8:
                raioDiametro()


def main():

    direcionado = int(input("1 - DIRECIONADO\n"
                         "2 - NÃO DIRECIONADO\n"
                         "valor: "))

    valorado = int(input("1 - VALORADO\n"
                         "2 - NÃO VALORADO\n"
                         "valor: "))

    opcao = int(checkOption(valorado, direcionado))
    criarGrafo(opcao)
    menu(opcao, valorado, direcionado)


if __name__ == '__main__':
    main()