from random import random

from parte_1.individuo import Individuo


class AlgoritmoGenetico:

    def __init__(self, tamanho_populacao, taxa_mutacao, numero_geracoes):
        self.numero_geracoes = numero_geracoes
        self.taxa_mutacao = taxa_mutacao
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = None

    def inicializar_populacao(self, espacos, valores, limite_espacos):
        """
        Cria indivíduos repassando os dados coletados.
        :param espacos: tamanhos dos produtos.
        :param valores: valores de venda dos produtos.
        :param limite_espacos: volume máximo para distribuir os produtos.
        :return: self
        """
        # Percorre os dados...
        for i in range(self.tamanho_populacao):
            # Cria o indivíduo da população inicializando seus dados.
            self.populacao.append(Individuo(espacos, valores, limite_espacos, nome=str(i + 1)))
        # Informa a melhor solução somente de forma figurativa.
        self.melhor_solucao = self.populacao[0]
        return self

    def ordena_populacao(self):
        """
        Faz a ordenação da população pela nota de avaliação de forma decrescente.
        :return:
        """
        # Executa a ordenação.
        self.populacao = sorted(
            self.populacao, key=lambda individuo: individuo.avaliacao().nota_avaliacao, reverse=True)
        return self

    def melhor_individuo(self, individuo):
        """
        Executa uma validação verificando, de acordo com a regra, qual a melhor solução e
        guarda esta informação.
        :param individuo: Indivíduo da população.
        :return: self
        """
        # Mede o indivíduo sobre a melhor solução.
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
        return self

    def soma_avaliacoes(self):
        """
        Calcula a soma das avaliações para utilizá-la no cálculo da proporção em que cada indivíduo
        tem sobre este total.
        :return:
        """
        soma = 0
        # Percorre todos os indivíduos.
        for individuo in self.populacao:
            # Totaliza as avaliações.
            soma += individuo.nota_avaliacao
        return soma

    def selecionar_pai(self):
        """
        Seleciona a localização do pai para a geração de uma nova população.
        :return: Localização do pai.
        """
        soma_avaliacao = self.soma_avaliacoes()
        # Recupera uma proporção randômica sobre a soma das avaliações.
        valor_sorteado = random() * soma_avaliacao
        pai = -1
        soma = 0
        i = 0
        # percorre a lista de indivíduos.
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai

    def visualizar_geracao(self):
        """
        Apresenta os dados do primeiro item da lista.
        :return: self
        """
        melhor = self.populacao[0]
        print(f'Geração: {melhor.geracao}, {melhor}, Nota: {melhor.nota_avaliacao}')
        return self

    def visualizar_melhor_resultado(self):
        """
        Apresenta o melhor resultado.
        :return: self
        """
        print(f'\nGeração: {self.melhor_solucao.geracao}')
        print(f'Melhor solução para o problema: {self.melhor_solucao}')
        print(f'Nota: {self.melhor_solucao.nota_avaliacao}')
        print(f'Soma das avaliações: {self.soma_avaliacoes()}')
        return self

    def resolver(self, espacos, valores, limite_espacos):
        """
        Seleciona a melhor solução para o problema.
        :param espacos: lista de espaços de cada produto.
        :param valores: lista de valores de cada produto.
        :param limite_espacos: valor total do espaço disponível para distribuir os produtos.
        :return: Melhor cromossomo que contem a informação da distribuição.
        """
        # Inicializa a população, faz a ordenação da inicialização e apresenta os dados.
        self.inicializar_populacao(espacos, valores, limite_espacos).ordena_populacao().visualizar_geracao()

        # Percorre as gerações.
        for geracao in range(self.numero_geracoes):
            # A cada geração cria uma nova população.
            nova_populacao = []
            # Recupero os novos indivíduos, 2 a 2.
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                # Seleciona os pais.
                pai1 = self.selecionar_pai()
                pai2 = self.selecionar_pai()
                # Gera filhos e aplica o crossover.
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                # Aplica a mutação nos filhos.
                nova_populacao.append(filhos[0].mutacao(self.taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(self.taxa_mutacao))

            # Recupera a população da nova geração.
            self.populacao = list(nova_populacao)
            # Re-organiza a nova população.
            self.ordena_populacao().visualizar_geracao().melhor_individuo(self.populacao[0])

        # Ao final das gerações apresenta os resultados.
        self.visualizar_melhor_resultado()

        return self.melhor_solucao.cromossomo
