#O mesmo professor agora quer sortear a ordem de apresentação dos alunos. Faça um programa que leia a
#o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle

def ordem(lista):
    shuffle(lista)
    print(lista)

ordem(['vinicius', 'renan', 'taina', 'gustavo'])