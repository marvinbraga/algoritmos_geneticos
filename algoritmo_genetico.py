from random import random

from individuo import Individuo


class AlgoritmoGenetico:

    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = None

    def inicializar_populacao(self, espacos, valores, limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos, nome=str(i + 1)))
        self.melhor_solucao = self.populacao[0]
        return self

    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, key=lambda individuo: individuo.avaliacao().nota_avaliacao,
                                reverse=True)
        return self

    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
        return self

    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma

    def selecionar_pai(self):
        soma_avaliacao = self.soma_avaliacoes()
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai

    def visualizar_geracao(self):
        melhor = self.populacao[0]
        print(f'Geração: {melhor.geracao}, {melhor}, Nota: {melhor.nota_avaliacao}')
        return self

    def resolver(self, taxa_mutacao, numero_geracoes, espacos, valores, limite_espacos):
        self.inicializar_populacao(espacos, valores, limite_espacos)
        self.ordena_populacao()
        self.visualizar_geracao()

        for geracao in range(numero_geracoes):
            nova_populacao = []
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.selecionar_pai()
                pai2 = self.selecionar_pai()
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))

            self.populacao = list(nova_populacao)
            self.ordena_populacao().visualizar_geracao().melhor_individuo(self.populacao[0])

        print(f'Geração: {self.melhor_solucao.geracao}')
        print(f'Melhor solução para o problema: {self.melhor_solucao}')
        print(f'Nota: {self.melhor_solucao.nota_avaliacao}')
        print(f'Soma das avaliações: {self.soma_avaliacoes()}')

        return self.melhor_solucao.cromossomo
