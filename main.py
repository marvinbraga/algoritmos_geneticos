from algoritmo_genetico import AlgoritmoGenetico
from individuo import Individuo
from produto import Produto


if __name__ == '__main__':
    lista_produtos = [
        Produto('Geladeira Dako', 0.751, 999.90),
        Produto('IPhone 6', 0.0000899, 2199.12),
        Produto('TV 55"', 0.400, 4346.99),
        Produto('TV 50"', 0.290, 3999.90),
        Produto('TV 42"', 0.200, 2999.90),
        Produto('Notebook Dell', 0.00350, 2499.90),
        Produto('Ventilador Panasonic', 0.496, 199.90),
        Produto('Microondas Eletrolux', 0.0424, 308.66),
        Produto('Microondas LG', 0.0544, 429.90),
        Produto('Microondas Panasonic', 0.0319, 299.29),
        Produto('Geladeira Brastemp', 0.635, 849.00),
        Produto('Geladeira Consul', 0.870, 1199.89),
        Produto('Notebook Lenovo', 0.498, 1999.90),
        Produto('Notebook Asus', 0.527, 3999.00),
    ]

    espacos = []
    valores = []
    nomes = []

    # Separa os atributos
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)

    # Limite da carga no caminhão
    limite = 3
    tam_populacao = 20

    # Pais mais capazes geram mais filhos e pais menos capazes também geram, porém, em menor quantiodade.
    nova_populacao = []
    taxa_mutacao = 0.01
    numero_geracoes = 100

    ag = AlgoritmoGenetico(tam_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, espacos, valores, limite)
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print(lista_produtos[i])
