import random

from django.shortcuts import render
from random import randint


def game(request):

    global placar_j, placar_c
    escolha = ""
    computador = ""
    resultado = ""



    if request.GET:

        CHOICES = ['Rock', 'Paper', 'Scissors']

        escolha = request.GET.get('choice')
        computador = random.choice(CHOICES)
        placar_j = request.GET('placar_jogador1')
        placar_c = request.GET('placar_computador')

        if escolha == computador:
            resultado = 'Empate'
        elif (escolha == 'Rock') & (computador == 'Scissors'):
            resultado = 'Jogador ganhou'
            placar_j += 1
        elif (escolha == 'Rock') & (computador == 'Paper'):
            resultado = 'Jogador Perdeu'
            placar_c += 1
        elif (escolha == 'Scissors') & (computador == 'Paper'):
            resultado = 'Jogador ganhou'
            placar_j += 1
        elif (escolha == 'Scissors') & (computador == 'Rock'):
            resultado = 'Jogador Perdeu'
            placar_c += 1
        elif (escolha == 'Paper') & (computador == 'Rock'):
            resultado = 'Jogador ganhou'
            placar_j += 1
        elif (escolha == 'Paper') & (computador == 'Scissors'):
            resultado = 'Jogador Perdeu'
            placar_c += 1

    context = {
        'jogador1' : escolha,
        'computador' : computador,
        'resultado' : resultado,
        'placar_jogador1' : placar_j,
        'placar_computador' : placar_c,
    }

    return render(request, 'rockpaperscissors2.html', context)
