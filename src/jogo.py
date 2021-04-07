import random

from src.jogadores import Jogadores
from src.tabuleiro import Tabuleiro


def popula_tabuleiro():
    tabuleiro_populado = []
    for casa in Tabuleiro.casas:
        custo_de_venda = random.randrange(300)
        valor_aluguel = random.randrange(100)
        proprietario = None
        casas_populadas = {
            'casa': casa,
            'propriedade': f'propriedade_{casa}',
            'custo_de_venda': custo_de_venda,
            'valor_aluguel': valor_aluguel,
            'proprietario': proprietario
        }
        tabuleiro_populado.append(casas_populadas)

    return tabuleiro_populado


def cria_jogadores():
    jogador1 = Jogadores("João", "impulsivo", 0)
    jogador2 = Jogadores("Maria", "exigente", 0)
    jogador3 = Jogadores("Ana", "cauteloso", 0)
    jogador4 = Jogadores("Pedro", "aleatório", 0)
    return [jogador1, jogador2, jogador3, jogador4]


def casa_no_tabuleiro(tabuleiro, numero_de_casas):
    return tabuleiro[numero_de_casas]


def compra_ou_aluga(propriedade, jogador):
    if not propriedade.get('proprietario'):
        comprado = jogador.compra(propriedade.get('custo_de_venda'), propriedade.get('valor_aluguel'))
        if 'comprado' in comprado:
            return 'Comprado'
        return 'Não Comprado'
    alugado = jogador.aluga(propriedade.get('valor_aluguel'))
    if 'alugado' in alugado:
        return 'Alugado'


def completou_a_volta_no_tabuleiro(jogador):
    jogador.ganha_saldo(100)


def avanca_no_tabuleiro(jogador, numero_de_casas, tabuleiro):
    if jogador.casa + numero_de_casas >= len(tabuleiro):
        ''' completou a volta no tabuleiro '''
        completou_a_volta_no_tabuleiro(jogador)
        jogador.casa = -1 + numero_de_casas
    jogador.casa += numero_de_casas
    return jogador.casa


def remove_jogador(jogador, jogadores):
    jogadores = jogadores.remove(jogador)
    return jogadores


def proxima_rodada(jogadores, tabuleiro, quantidade_de_jogadores, vencedor):
    for jogador in jogadores:
        ''' verifica se o jogador já perdeu o jogo'''
        if jogador.consulta_saldo() < 0:
            jogadores = remove_jogador(jogador, jogadores)
            print(f'{jogador.nome} - saldo {jogador.saldo}')

        if len(jogadores) == 1:
            vencedor = jogador.nome
            print(f'O jogador: {vencedor}, venceu!!!')
        elif rodada == 1000:

            return vencedor

        ''' joga dado '''
        numero_de_casas = jogador.joga_dado()

        ''' avança no tabuleiro '''
        jogador.casa = avanca_no_tabuleiro(jogador, numero_de_casas, tabuleiro)

        ''' avançando nas casas'''
        propriedade = casa_no_tabuleiro(tabuleiro, jogador.casa)

        ''' Tenta comprar ou alugar'''
        jogada = compra_ou_aluga(propriedade, jogador)

        ''' atualizando tabuleiro '''
        if 'comprado' in jogada:
            tabuleiro[jogador.casa]['proprietario'] = jogador.nome

    print(f'rodada {rodada} - qtd jogadores {quantidade_de_jogadores}')
    return vencedor


def rodada():
    ''' Carrega jogadores '''
    jogadores = cria_jogadores()
    ''' cria tabuleiro'''
    tabuleiro = popula_tabuleiro()
    ''' casa inicial - sempre 1'''
    quantidade_de_jogadores = 4
    ''' inicio do jogo '''
    vencedor = None
    rodada = 0
    while not vencedor:
        vencedor = proxima_rodada(jogadores, tabuleiro, quantidade_de_jogadores, vencedor)
        rodada += 1
        if rodada == 10 or vencedor is not None:
            break


if __name__ == '__main__':
    rodada()
