#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
def aplicar_desconto():
    preco = float(input('Preço: '))
    print(f'O valor do produto com desconto é igual a {preco - preco*0.05:.2f} reais')

aplicar_desconto()