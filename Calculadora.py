print ('Calculadora para a nota média')

aluno = input('Digite o nome do aluno:')

print (aluno)

print ('Digite as notas')

nota_1 = float(input('1º Nota:'))
nota_2 = float(input('2º Nota:'))
nota_3 = float(input('3º Nota:'))
nota_4 = float(input('4º Nota:'))

notas = (nota_1 + nota_2 + nota_3 + nota_4)
media = (notas/4)

if media >= 5: 
    print (f'{aluno} passou.')
else:
    print (f'{aluno} reprovou.')
print ('Sua nota foi:',media)
input()