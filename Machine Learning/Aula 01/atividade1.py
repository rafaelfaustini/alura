# Nesse projeto será classificado se um animal é um porco ou um cachorro
# Por meio de características, no caso, se o animal é gordinho, tem perna curta
# ou se late



porco1 = [1,1,0] # [Tem perna curta, é gordinho mas não late
porco2 = [1,1,0]
porco3 = [1,1,0]

cachorro1 = [1,1,1]
# Os outros dois cachorros nao são gordinhos mas ainda são cachorros
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# 1 para os porcos e -1 para os cachorros
marcacoes = [1, 1, 1, -1, -1, -1]

# É gordinho, tem perninha curta e late, será um cachorro ou um porco ?
descobrir1 = [1,1,1]
descobrir2 = [1,0,1]
descobrir3 = [1,0,0]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

testes = [descobrir1, descobrir2, descobrir3]
resultado = modelo.predict(testes)

for i in range(0, len(testes)):    
    if resultado[i] == -1:
        print("[Teste %d] É um cachorro !!" % (i+1))
    else:
        print("[Teste %d] É um porco !!" % (i+1))
