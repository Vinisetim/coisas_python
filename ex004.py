#mostrar o tipo e algumas informações de um valor digitado

def infos():
    valor = (input('Digite um valor: '))
    print(f'O valor {valor} \n é do tipo: {type(valor)},\n é númerico? {valor.isnumeric()}, \n é alfanumérico? {valor.isalnum()}, \n é decimal? {valor.isdecimal()}')

infos()