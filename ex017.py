#faça um programa que leia o comprimento do cateto oposto de um triangulo e do cateto adjacente
#de um triangulo e mostre o comprimento da hipotenusa
from math import hypot
def mostrar_hipotenusa():
    cateto_oposto = float(input("Digite o cateto oposto: "))
    cateto_adjacente = float(input("Digite o cateto adjacente: "))
    print(f"A Hipotenusa é igual á: {hypot(cateto_oposto, cateto_adjacente):.2f}")

mostrar_hipotenusa()