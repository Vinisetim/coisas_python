#Escreva um programa que converta uma temperatura digita em graus celsius para graus fahrenheit
def celcius_to_fahrenheit():
    temp = float(input('Digite a temperatura em fahrenheit: '))
    print(f"A temperatura em fahrenheit são {(temp*(9/5))+32}")

celcius_to_fahrenheit()

