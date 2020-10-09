from random import random


class Individuo:

    def __init__(self, espacos, valores, limite_espacos, geracao=0, nome=''):
        self.nome = nome
        self.descricao = 'Indivíduo' + nome
        self.geracao = geracao
        self.limite_espacos = limite_espacos
        self.valores = valores
        self.espacos = espacos
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.cromossomo = []
        self.inicializar_cromossomo()

    def __str__(self):
        return f'\nDescrição: {self.descricao}, ' \
               f'Cromossomo: {self.cromossomo}'
        # f'Espaços: {self.espacos} \n' \
        # f'Valores: {self.valores} \n' \

    def resumo(self, lista_produtos):
        print('\nComponentes da Carga:')
        for i in range(len(lista_produtos)):
            if self.cromossomo[i] == '1':
                print(lista_produtos[i])

        print(f'Valor Total da Carga: R$ {self.valor_total}')
        print(f'Volume Total da Carga: {self.volume_total} m3')
        print(f'Nota: {self.avaliacao().nota_avaliacao}')
        return self

    def inicializar_cromossomo(self):
        for i in range(len(self.espacos)):
            if random() < 0.5:
                self.cromossomo.append('0')
            else:
                self.cromossomo.append('1')

    @property
    def valor_total(self):
        total = 0
        for i in range(len(self.valores)):
            if self.cromossomo[i] == '1':
                total += self.valores[i]
        return total

    @property
    def volume_total(self):
        total = 0
        for i in range(len(self.espacos)):
            if self.cromossomo[i] == '1':
                total += self.espacos[i]
        return total

    def avaliacao(self):
        """
        Maximizar a configuração que devolver o maior valor total.
        :return:
        """
        nota = self.valor_total
        self.espaco_usado = self.volume_total
        if self.espaco_usado > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        return self

    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        geracao = self.geracao + 1
        filhos = [
            Individuo(self.espacos, self.valores, self.limite_espacos, geracao),
                      # nome=f'{outro_individuo.nome}{self.nome}.{geracao}'),
            Individuo(self.espacos, self.valores, self.limite_espacos, geracao),
                      # nome=f'{self.nome}{outro_individuo.nome}.{geracao}'),
        ]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos

    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        return self
