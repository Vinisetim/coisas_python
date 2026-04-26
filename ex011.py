#Crie um programa que leia a largura e a altura de uma parede em metros, calcula sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m^2

def quanta_tinta():
    altura = float(input('Altura da parede '))
    largura = float(input('Largura da parede '))
    area = altura * largura
    print(f'Para pintar uma parede com {area} metros, será necessário {area/2} litros de tinta')

quanta_tinta()