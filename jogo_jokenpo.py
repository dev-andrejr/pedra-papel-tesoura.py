from random import randint

v = 0
p = 0
e = 0
r = 'teste'


def contador():
    global v, p, e, r
    if r == 'Você venceu!!!':
        v += 1
    elif r == 'Você perdeu!':
        p += 1
    elif r == 'Empate!':
        e += 1
    print(f'{v}, {p}, {e}')


def escolha():
    print('[1] - SIM\n[2] - Não')

    def certeza():
        print('[1] - sim')
        print('[2] - não')
        c = int(input('Você tem certeza? '))
        if c == 1:
            contador()
            print(
                f'Tchau! Você teve:\n{v} vitórias\n{p} derrotas\n{e} Empates\nAté a próxima...')
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
    pc = randint(1, 3)
    global r
    print('''Escolha entre
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura ''')
    player = int(input('Qual sua jogada:'))
    print('-=' * 12)
    print(f'A máquina escolheu {item[pc]}')
    print(f'Você escolhe {item[player]}')
    print('-=' * 12)
    if pc == 1:  # Máquina escolheu Pedra
        if player == 1:
            r = 'Empate!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 2:
            r = 'Você venceu!!!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 3:
            r = 'Você perdeu!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        else:
            print('Comando inválido')
            print('-' * 12)
            escolha()

    elif pc == 2:  # Máquina escolheu Papel
        if player == 1:
            r = 'Você perdeu!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 2:
            r = 'Empate!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 3:
            r = 'Você venceu!!!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        else:
            print('Comando inválido')
            print('-' * 12)
            escolha()

    elif pc == 3:  # Máquina escolheu Tesoura
        if player == 1:
            r = 'Você venceu!!!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 2:
            print('Você perdeu!')
            print('-' * 12)
            contador()
            escolha()
        elif player == 3:
            r = 'Empate!'
            print(f'{r}')
            print('-' * 12)
            contador()
            escolha()
        else:
            print('Comando inválido')
            escolha()


escolha()
