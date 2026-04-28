#Um professor quer sortear um dos seus alunos para apagar o quadro. faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido
from random import choice
def sorteio(lista):
    print(choice(lista))

sorteio(['renan', 'vinicius', 'taina', 'gustavo'])