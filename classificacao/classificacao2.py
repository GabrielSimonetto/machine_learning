from aula2 import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X, Y = carregar_acessos()

modelo = MultinomialNB()

divisorX = len(X)/2

treinoX = X[:90]
testeX = X[90:]

treinoY = Y[:90]
testeY = Y[90:]

modelo.fit(treinoX, treinoY)
resultado = modelo.predict(testeX)

diferencas = resultado - testeY

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)

taxa_de_acerto = 100.0 * total_de_acertos / len(testeX)

print(taxa_de_acerto)