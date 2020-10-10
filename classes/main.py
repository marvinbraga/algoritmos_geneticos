from classes.algoritmo_genetico import AlgoritmoGenetico
from classes.connect import Connect

if __name__ == '__main__':
    espacos = []
    valores = []
    nomes = []
    lista_produtos = Connect().instanciar_objetos().lista_produtos
    # Separa os atributos
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)

    # Limite da carga no caminhão
    limite = 3.0
    tam_populacao = 20
    numero_geracoes = 2000
    # Pais mais capazes geram mais filhos e pais menos capazes também geram, porém, em menor quantidade.
    taxa_mutacao = 0.01

    ag = AlgoritmoGenetico(tam_populacao, taxa_mutacao, numero_geracoes)
    resultado = ag.resolver(espacos, valores, limite)
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print(lista_produtos[i])

    ag.apresenta_grafico_melhores()
