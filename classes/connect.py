import os
import pymysql

from classes.produto import Produto


class Connect:

    def __init__(self):
        self.lista_produtos = []
        self._get_connect()

    def __del__(self):
        self._conn.close()

    @property
    def conn(self):
        return self._conn

    def _get_connect(self):
        self._conn = pymysql.connect(
            host=os.environ.get('MYSQL_HOST', default='localhost'),
            user=os.environ.get('MYSQL_USER', default='admin'),
            passwd=os.environ.get('MYSQL_PASSWORD', default='Raposa789'),
            db=os.environ.get('MYSQL_DATABASE', default='produtos-db')
        )
        return self

    def _exec_sql(self, cursor, query):
        print(query)
        cursor.execute(query)
        return self

    def instanciar_objetos(self):
        self.lista_produtos = []
        cursor = self._conn.cursor()
        try:
            self._exec_sql(
                cursor,
                'SELECT nome, espaco, valor, quantidade from produtos;'
            )
            for prd in cursor:
                self.lista_produtos.append(
                    Produto(prd[0], prd[1], prd[2], prd[3])
                )
        finally:
            cursor.close()
        return self

    def inserir_produto(self, prd, cursor=None, commit=True):
        cr = cursor
        if cursor is None:
            cr = self._conn.cursor()
        try:
            self._exec_sql(
                cr,
                "INSERT INTO produtos (nome, espaco, valor, quantidade) VALUES " +
                f"('{prd.nome}', {prd.espaco}, {prd.valor}, 1);"
            )
        finally:
            if commit:
                self._conn.commit()
            if cursor is None:
                cr.close()
        return self

    def _criar_produtos(self):
        if self._verificar_registros():
            return self

        cursor = self._conn.cursor()
        try:
            for prd in self.lista_produtos:
                self.inserir_produto(prd, cursor, False)
            self._conn.commit()
            print(f'{len(self.lista_produtos)} foram cadastrados.')
        finally:
            cursor.close()
        return self

    def _verificar_registros(self):
        result = False
        cursor = self._conn.cursor()
        try:
            self._exec_sql(
                cursor,
                'SELECT COUNT(*) FROM produtos;'
            )
            for rs in cursor:
                result = rs[0] > 0
        finally:
            cursor.close()
        return result

    def moke(self):
        self.lista_produtos = [
            Produto('Geladeira Dako', 0.751, 999.90),
            Produto('IPhone 6', 0.0000899, 2199.12),
            Produto('TV 55"', 0.400, 4346.99),
            Produto('TV 50"', 0.290, 3999.90),
            Produto('TV 42"', 0.200, 2999.90),
            Produto('Notebook Dell', 0.00350, 2499.90),
            Produto('Ventilador Panasonic', 0.496, 199.90),
            Produto('Micro-ondas Eletrolux', 0.0424, 308.66),
            Produto('Micro-ondas LG', 0.0544, 429.90),
            Produto('Micro-ondas Panasonic', 0.0319, 299.29),
            Produto('Geladeira Brastemp', 0.635, 849.00),
            Produto('Geladeira Consul', 0.870, 1199.89),
            Produto('Notebook Lenovo', 0.498, 1999.90),
            Produto('Notebook Asus', 0.527, 3999.00),
        ]
        self._criar_produtos()
