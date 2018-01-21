from random import randint

random = randint(0, 100)
tentativa = input('Chute um número de 0 á 100: ')
if tentativa == random:
    print ('Voce acertou! Parabens.')
else:
    print ('Voce errou, tente novamente.')
