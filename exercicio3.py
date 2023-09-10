# Exercício Erros e Exceções

def calcular_media(valores):
    tamanho = 1
    soma = 0.0
    for valor in valores:
        soma += valor
        media = soma / tamanho
        return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))

