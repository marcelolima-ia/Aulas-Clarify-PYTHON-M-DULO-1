from random import randint

print('############ Iniciando Jogo#############')

valorminimo = 0
valormaximo = 100
random = randint (valorminimo, valormaximo)
chute = 0
chances = 10

while chute != random:
    chute = input(f'chute um numero entre {valorminimo} a {valormaximo}\n')
    if chute.isnumeric():
        chute = int(chute)
        chances -= 1
        if chute == random:
            print('-----')
            print('Parabéns, você venceu! O numero era{} e voce ainda tinha {} chances.'.format(random, chances))
            print('-----')
            break
        else:
            print('')
            if chute > random:
                print('Você ERROU!! Dica: É um numero menor.')
            else: 
                print('Você ERROU!! Dica: É um numero maior.')
            print(f'Você ainda possui {chances} chances')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você errou, o numero era {}'.format(random))
            print('')
            break

print('############ FIM DO JOGO #############')