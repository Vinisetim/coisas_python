#Crie um programa que leia um número e mostre o seu dobro, tripo e raiz quadrada

def dobro_tripo_raiz():
    num = int(input('Escreva um valor: '))
    print(f'O dobro do número {num} é {num * 2}, O triplo é {num * 3} e a raiz é {num **(1/2):.4f}')

dobro_tripo_raiz()