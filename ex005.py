#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e o seu antecessor

def antecessor_sucessor():
    num = int(input('Digite um numero: '))
    print(f'O sucessor do número {num} é  {num + 1}, E o antecessor é {num - 1}')

antecessor_sucessor()