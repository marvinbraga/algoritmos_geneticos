import random

import matplotlib.pyplot as plt
import numpy as np
from deap import base, creator, algorithms, tools

from classes.connect import Connect

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

toolbox = base.Toolbox()
# Definição da função de avaliação.
creator.create('FitnessMax', base.Fitness, weights=(1.0,))
# Criar o indivíduo
creator.create('Individual', list, fitness=creator.FitnessMax)
toolbox.register('attr_bool', random.randint, 0, 1)
# Criação dos indivíduos.
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(espacos))
# Definição da população.
toolbox.register('population', tools.initRepeat, list, toolbox.individual)


def avaliacao(individual):
    nota = 0
    soma_espacoes = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            nota += valores[i]
            soma_espacoes += espacos[i]
    if soma_espacoes > limite:
        nota = 1
    return nota / 100000,


toolbox.register('evaluate', avaliacao)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutFlipBit, indpb=0.01)
toolbox.register('select', tools.selRoulette)

if __name__ == '__main__':

    random.seed(1)
    populacao = toolbox.population(n=20)
    probabilidade_crossover = 1.0
    probabilidade_mutacao = 0.01
    numero_geracoes = 100

    estatisticas = tools.Statistics(key=lambda individuo: individuo.fitness.values)
    estatisticas.register('max', np.max)
    estatisticas.register('min', np.min)
    estatisticas.register('med', np.mean)
    estatisticas.register('std', np.std)

    populacao, info = algorithms.eaSimple(populacao, toolbox, probabilidade_crossover, probabilidade_mutacao,
                                          numero_geracoes, estatisticas)

    melhores = tools.selBest(populacao, 2)
    for individuo in melhores:
        print(individuo)
        print(individuo.fitness)
        soma = 0
        for i in range(len(lista_produtos)):
            if individuo[i] == 1:
                soma += valores[i]
                print(individuo, soma)

    valores_grafico = info.select('max')
    plt.plot(valores_grafico)
    plt.title('Acompanhamento dos valores')
    plt.show()
