from random import randint

vitorias = perdas = empates = 0
resultado = 'n'


def contador():
    global vitorias, perdas, empates, resultado
    if resultado == 'Você venceu!!!':
        vitorias += 1
    elif resultado == 'Você perdeu!':
        perdas += 1
    elif resultado == 'Empate!':
        empates += 1


def escolha():
    def certeza():
        print('\nVocê tem certeza? ')
        print('    [1] - sim')
        c = int(input('    [2] - não\n'))
        if c == 1:
            print('\n', '-' * 16)
            print(f'Tchau! Você teve:')
            print('-=' * 9)

            if vitorias == 0:
                print('Nenhuma vitória')
            elif vitorias == 1:
                print(f'{vitorias} vitória')
            else:
                print(f'{vitorias} vitórias')

            if perdas == 0:
                print('Nenhuma derrota')
            elif perdas == 1:
                print(f'{perdas} derrota')
            else:
                print(f'{perdas} derrotas')

            if empates == 0:
                print('Nenhum empate')
            elif empates == 1:
                print(f'{empates} Empate')
            else:
                print(f'{empates} Empates')

            print('-=' * 9)
            print()
            print('Até a próxima...')
        elif c == 2:
            escolha()
    print('Você quer jogar Pedra, Papel, Tesoura:')
    opção = int(input('    [1] - SIM\n    [2] - Não\n'))
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
    global resultado
    print('\nQual sua jogada?')
    print('    [1] - Pedra')
    print('    [2] - Papel')
    player = int(input('    [3] - Tesoura\n'))
    print('-=' * 12)
    print(f'A máquina escolheu {item[pc]}')
    print(f'Você escolhe {item[player]}')
    print('-=' * 12)

    if pc == 1:  # Máquina escolheu Pedra
        if player == 1:
            resultado = 'Empate!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 2:
            resultado = 'Você venceu!!!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 3:
            resultado = 'Você perdeu!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        else:
            print('Comando inválido')
            print('-' * 12)
            escolha()

    elif pc == 2:  # Máquina escolheu Papel
        if player == 1:
            resultado = 'Você perdeu!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 2:
            resultado = 'Empate!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 3:
            resultado = 'Você venceu!!!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        else:
            print('Comando inválido')
            print('-' * 12)
            escolha()

    elif pc == 3:  # Máquina escolheu Tesoura
        if player == 1:
            resultado = 'Você venceu!!!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 2:
            resultado = 'Você perdeu!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        elif player == 3:
            resultado = 'Empate!'
            print(f'{resultado}')
            print('-' * 12)
            contador()
            escolha()
        else:
            print('Comando inválido')
            escolha()


escolha()
