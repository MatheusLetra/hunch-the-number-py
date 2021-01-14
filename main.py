#!python3

from game import config_game
from game import header_game
from game import random_number

header_game.header(config_game.initial_number,config_game.final_number)

number = random_number.randomize(config_game.initial_number,config_game.final_number)


hunch = 0

while hunch != number:
    while hunch < config_game.initial_number or hunch > config_game.final_number:
        try:
            hunch = int(input('Informe seu palpite:'))
        except:
            hunch = 0
        if hunch < config_game.initial_number or hunch > config_game.final_number: 
            print("Seu palpite não é um número inteiro válido!")
            print(f'Você deve informar um valor inteiro entre {config_game.initial_number} e {config_game.final_number}')
    
    if hunch > number:
        hunch = 0
        print('O seu palpite é maior que o número secreto!')
    elif hunch < number:
        hunch = 0
        print('O seu palpite é menor que o número secreto!')
    else:
        print('Parabéns Você Acertou o Número Secreto!')
        if input('Deseja jogar novamente? (Sim / Não)')  == 'Sim':
            hunch = 0
            number = random_number.randomize(config_game.initial_number,config_game.final_number)

print('Fim do Jogo!')
