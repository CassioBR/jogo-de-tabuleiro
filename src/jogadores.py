import random


class Jogadores():
    def __init__(self, nome, comportamento, casa):
        self.saldo = 300
        self.nome = nome
        self.comportamento = comportamento
        self.casa = casa

    def compra(self, preco_compra, valor_aluguel):
        if self.comportamento == 'impulsivo' and self.saldo >= preco_compra:
            self.saldo = self.saldo - preco_compra
            return 'comprado'
        elif self.comportamento == 'exigente' and self.saldo >= preco_compra and valor_aluguel > 50:
            self.saldo = self.saldo - preco_compra
            return 'comprado'
        elif self.comportamento == 'cauteloso' and self.saldo - preco_compra >= 80:
            self.saldo = self.saldo - preco_compra
            return 'comprado'
        elif self.comportamento == 'aleatório' and self.saldo >= preco_compra:
            compra_ou_nao = random.choice(['sim', 'nao'])
            if 'sim' in compra_ou_nao:
                self.saldo = self.saldo - preco_compra
                return 'comprado'
        return 'Não Comprado'

    def aluga(self, preco):
        self.saldo = self.saldo - preco
        return 'alugado'

    def joga_dado(seld):
        return random.randrange(1, 7)

    def ganha_saldo(self, valor):
        self.saldo = self.saldo + valor

    def consulta_saldo(self):
        return self.saldo

