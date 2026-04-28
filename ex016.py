#Crie um programa que leia um número Real qualquer e mostra a sua porção inteira
from math import trunc
def porcao_inteira():
    """Essa função usa o módulo trunc da biblioteca Math para fazer um exemplo de uso, mas a mesma
    solução funciona se fazer a conversão de valor para int"""
    num = float(input("Escreva um número real: "))
    print(f"A porção inteira desse número é {trunc(num)}")

porcao_inteira()