import csv

def ler_acessos():
    x = []
    y = []

    arquivo = open('include/acesso.csv', 'r')
    leitor = csv.reader(arquivo)

    #Descarta a primeira linha com as strings
    next(leitor)

    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        x.append([acessou_home, acessou_como_funciona, acessou_contato, comprou])
        y.append(comprou)
    return x,y

                   
