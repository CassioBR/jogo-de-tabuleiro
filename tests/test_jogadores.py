from src.jogadores import Jogadores


def test_jogadores():
    jogador = Jogadores('jogador1')
    assert jogador.saldo == 300
    assert jogador.nome == 'jogador1'
