from src.jogadores import Jogadores
from src.jogo import popula_tabuleiro, casa_no_tabuleiro, remove_jogador
# import ipdb


# def test_casa_no_tabuleiro():
#     tabuleiro = popula_tabuleiro()
#     num_casas = 1
#     casa = casa_no_tabuleiro(tabuleiro[19], num_casas)
#     print(casa)
#     assert casa == 0


def test_remove_jogador():
    jogador_teste = Jogadores("Teste", "impulsivo", 0)
    jogador_teste1 = Jogadores("Teste1", "impulsivo", 0)
    jogadores = [jogador_teste, jogador_teste1]
    jogador_teste1.saldo = -1
    # ipdb.set_trace()

    for jogador in jogadores:
        if jogador.consulta_saldo() < 0:
            jogadores = remove_jogador(jogador, jogadores)
    assert len(jogadores) == 1
