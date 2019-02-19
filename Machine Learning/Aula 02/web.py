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
