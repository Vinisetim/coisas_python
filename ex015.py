#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
# de dias pelo qual ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia
# e 0.15 reais por km rodado

def valor_aluguel():
    km = float(input("Qual a quantidade de km: "))
    dias = int(input("Qual a quantidade de dias: "))
    print(f"Rodando {km} Km por {dias} dias, o Valor do aluguel sai {60*dias + km*0.15} reais")

valor_aluguel()