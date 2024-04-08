#Desenvolva um programa e leia as duas notas de um aluno, calcule a sua note media
nota1 = float(input("Qual o foi a nota da primeira avaliação?"))
nota2 = float(input('Qual foi a nota da sua segunda avaliação?'))
media1 = nota1 + nota2
media2 = media1 / 2
print('Esta é a sua nota media:', media2)
if media2 < 6:
    print('Infelizmente voce nao foi aprovado.')
else:
    print('Aprovado!')
