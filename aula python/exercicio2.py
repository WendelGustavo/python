#2)Faça um programa que receba a o peso se uma pessoa e sua altura. Posteriormente calcule o seu IMC, e exiba em qual classificação a pessoa se enquadra.

#CLASSIFICAÇÂO
#17.0 - 18.4             Magreza grau I
#18.5 - 24.9             Adequado
#25.0 - 29.9             Pré-obeso
#30.0 - 34.9            Obesidade grau I

peso = float(input('Qual é seu peso?'))
altura = float(input('Qual é sua altura?'))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))

if imc <17.0:
    print('Abaixo do peso normal')

elif 17.0 <= imc < 18.4:
  print('Magreza Grau I')

elif 18.5 <= imc < 24.9:
  print('Adequado')

elif 25.0<= imc < 29.9:
  print('Pré-obeso')

elif 30.0 <= imc < 34.9:
  print('Obesidade Grau I')