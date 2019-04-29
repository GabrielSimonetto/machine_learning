import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv','rt')
    leitor = csv.reader(arquivo)

    #joga fora a primeira linha
    next(leitor)

    for (acessou_home, acessou_como_funciona, 
            acessou_contato, comprou) in leitor:

        X.append([int(acessou_home),
                    int(acessou_como_funciona),
                    int(acessou_contato)])

        Y.append(int(comprou))

    return X, Y