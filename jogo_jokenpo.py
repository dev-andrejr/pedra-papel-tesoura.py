from random import randint
def escolha():
    print('''[1] - SIM
[2] - Não''')
    def certeza():
        print('[1] - sim')
        print('[2] - não')
        c = int(input('Você tem certeza? '))
        if c == 1:
            print('Tchau!')
        elif c == 2:
            escolha()
    opção = int(input('Você quer jogar Pedra, Papel, Tesoura:'))
    if opção == 1:
        jogar()
    elif opção == 2:
        certeza()
    else:
        print('Comando Inválido')
        escolha()

def jogar():
    item = ['n', 'Pedra', 'Papel', 'Tesoura']
    pc = randint(1,3)
    print('''Escolha entre
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura ''')
    player = int(input('Qual sua jogada:'))
    print('-=' * 12)
    print(f'A máquina escolheu {item[pc]}')
    print(f'Você escolhe {item[player]}')
    print('-=' * 12)
    if pc == 1: # Máquina escolheu Pedra
        if player == 1:
            print('Empate!')
            print('-' * 12)
            escolha()
        elif player == 2:
            print('Você venceu!')
            print('-' * 12)
            escolha()
        elif player == 3:
            print('Você perdeu!')
            print('-' * 12)
            escolha()
        else:
            print('Comando inválido')
            print('-' * 12)
            escolha()
    elif pc == 2: # Máquina escolheu Papel
        if player == 1:
            print('Você perdeu')
            print('-' * 12)
            escolha()
        elif player == 2:
            print('Empate')
            print('-' * 12)
            escolha()
        elif player == 3:
            print('Você vence')
            print('-' * 12)
            escolha()
        else:
            print('Comando inválido')
            print('-' * 12)
            escolha()
    elif pc == 3: # Máquina escolheu Tesoura
        if player == 1:
            print('Você venceu!')
            print('-' * 12)
            escolha()
        elif player == 2:
            print('Você perdeu!')
            print('-' * 12)
            escolha()
        elif player == 3:
            print('Empate!')
            print('-' * 12)
            escolha()
        else:
            print('Comando inválido')
            escolha()

escolha()
