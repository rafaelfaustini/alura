import csv

def ler_acessos():
    dados = []
    marcacoes = []

    arquivo = open('include/acesso.csv', 'r')
    leitor = csv.reader(arquivo)

    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        dados.append([acessou_home, acessou_como_funciona, acessou_contato, comprou])
        marcacoes.append(comprou)
    return dados,marcacoes



                   
