import sys
import random
from rich import print
from ultilidades import jogo

print('dificuldade (1/2/3)')
dificuldade = int(input('escolha a dificuldade: '))


if dificuldade == 1:
    print('Você escolheu o modo [#7FFFD4]facil[/#7FFFD4] (noob)')
    jogo(1)
elif dificuldade == 2:
    print('Você escolheu o modo [#7fff00]medio[/#7fff00] (nhe)')
    jogo(2)
elif dificuldade == 3:
    print('Você escolheu o modo [#e32636]dificil[/#e32636], inteligencia ou tolice?')
    jogo(3)
else:
     print('escolha uma dificuldade valida: ')
     




        