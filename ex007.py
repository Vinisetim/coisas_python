#Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua méda
def media():
    num = int(input('Nota1: '))
    num2 = int(input('Nota2: '))
    print(f'A média do Aluno foi {(num + num2)/2}')

media()