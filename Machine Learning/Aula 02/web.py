import csv

def ler_acessos():
    x = []
    y = []

    arquivo = open('include/acesso.csv', 'r')
    leitor = csv.reader(arquivo)

    #Descarta a primeira linha com as strings
    next(leitor)

    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        x.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
        y.append(int(comprou))
    return x,y

def valida(r):
    if(r.isdigit()):
        r = int(r)
    if(r == 0 or r == 1):
        return True
    print("Houve um erro em uma das resposta do teste, refaça o mesmo. Certifique-se que digitou 0 ou 1")
    print("\n")
    return False
            

def dadosPrever():
    print("Será que vamos prever se o cliente comprou ?")
    testes = []
    while True:
        teste = []
        r = input("Acessou a home do site ? (0/1)\n")
        if(not valida(r)):
          continue
        teste.append(int(r))
        
        r = input("Acessou a página 'Como Funciona' ? (0/1)\n")
        if(not valida(r)):
          continue
        teste.append(int(r))
        
        r = input("Acessou a página 'Contato' ? (0/1)\n")
        if(not valida(r)):
          continue
        teste.append(int(r))

        testes.append(teste)
        r = input("Deseja inserir mais um teste ? (s)\n")
        if(r != 's' or r!= 'S'):
            return testes
def taxa_acerto(m, x, y):
    resultado = m.predict(x)
    diferencas = resultado - y
    acertos = [d for d in diferencas if d==0]
    total_acertos = len(acertos)
    total_elementos = len(x)
    taxa = 100.0 * total_acertos/total_elementos
    print("A taxa de acerto é de %.2f%%" % taxa)
    
def modelo_preditivo(dados_prever):
    X,Y = ler_acessos()

    pedacoTreino = round(len(X)*0.9)
    dadosTreino = X[:pedacoTreino]
    marcacoesTreino = Y[:pedacoTreino]

    pedacoTeste = round(len(X)-pedacoTreino)
    dadosTeste = X[-pedacoTeste:]
    marcacoesTeste = Y[-pedacoTeste:]


    
    from sklearn.naive_bayes import MultinomialNB

    modelo = MultinomialNB()
    modelo.fit(dadosTreino,marcacoesTreino)
    taxa_acerto(modelo, dadosTeste, marcacoesTeste)
    return modelo.predict(dados_prever)

def resultado(res):
    for i in range(0, len(res)):    
        if res[i] == 1:
            print("[Teste %d] Acho que vai comprar !!" % (i+1))
        else:
            print("[Teste %d] Acho que não vai comprar !!" % (i+1))
def prever():
    dados = dadosPrever()
    res = modelo_preditivo(dados)
    resultado(res)

prever()
