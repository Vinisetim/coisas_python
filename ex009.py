#faça um programa que leia um número inteiro e exiba a sua tabuada
def tabuada():
    num = int(input('Numerador: '))
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')

tabuada()