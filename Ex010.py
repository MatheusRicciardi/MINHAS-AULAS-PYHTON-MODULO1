#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
#Considerando 1 Dolar a 3,27 reais

carteira_reais = int(input('Digite aqui quantos reais voce gostaria de converter:'))
carteira_dolar = carteira_reais / 3.27

print('Com essa quantia em sua conta, voce poderá comprar {} em dolares'.format(carteira_dolar))
