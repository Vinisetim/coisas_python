#Faça um programa que leia um Ângulo qualquer e mostre na tela o seu seno cosseno e tangente
from math import sin, cos, tan, radians
def sin_cos_tan():
    angulo = float(input("Digite um angulo qualquer: "))
    angulo_rad = radians(angulo)
    print(f"O Sen é {sin(angulo_rad):.2f},\n o Cos é {cos(angulo_rad):.2f} \n e a tangente é {tan(angulo_rad):.2f}")

sin_cos_tan()
