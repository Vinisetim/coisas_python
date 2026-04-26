#crie um programa que retorne quantos centimetros e milimetros tem em X metros
def contagem():
    metros = int(input('Metros: '))
    print(f'Em {metros} metros existem {metros * 100} centimetros e {metros * 1000} milimetros ')

contagem()