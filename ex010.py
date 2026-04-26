#Crie um programa que leia quantos reias uma pessoa tem e mostro quantos dólares ela pode comprar (dado 1 dolar = 3,27 reaias)

def dolar():
    valor = float(input('Quantos reais: '))
    if valor : print(f"Você pode comprar {valor / 3.27:.2f} dólares")
    else: print("Você não pode comprar nenhum dólar, trabalhe")

dolar()