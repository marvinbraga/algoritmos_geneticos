class Produto:

    def __init__(self, nome, espaco, valor):
        self.valor = valor
        self.espaco = espaco
        self.nome = nome

    def __str__(self):
        return f'Nome: {self.nome}, Espaço: {self.espaco}, Valor: {self.valor}'
