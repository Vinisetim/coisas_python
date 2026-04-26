#Faça um algoritmo que mostra o salário de um funcionário com 15% de aumento
def aplicar_aumento():
    salario = float(input('Qual o seu salario: '))
    print(f'O valor do seu salario com aumento será {salario * 1.15:.2f} reais')

aplicar_aumento()