#1)Faça um programa que receba três notas de um aluno. A soma das três notas  pode alcançar o máximo de  dez pontos. Ou seja,  a primeira nota vale três pontos, a segunda nota vale três pontos e terceira nota vale quatro pontos.  Informe ainda se o aluno está ou não aprovado. Para um aluno estar aprovado é necessário atingir pelo menos seis pontos.
print('Saiba se você passou de ano:')
nota1 = float(input('Primeira nota'))
nota2 = float(input('Segunda nota'))
nota3 = float(input('Terceira nota'))
media = (nota1 + nota2 + nota3) / 3
print ('Tirando {:.1f}, {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, nota3, media))

if 6 > media:
    print('Você foi REPROVADO, .')

elif 6 < media:
    print('Você foi APROVADO,!.')