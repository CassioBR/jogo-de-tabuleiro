from src.tabuleiro import Tabuleiro


def test_tabuleiro():
    tabuleiro_propriedade = Tabuleiro.casas
    numero_de_casas = tuple(range(1, 21))
    assert numero_de_casas == tabuleiro_propriedade
