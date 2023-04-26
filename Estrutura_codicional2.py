''' Crie um programa onde o usuario solicita um numero e veja se o numero
é maior que 0, menor que 0 ou igual a 0
'''

num = float(input("Digite um número:"))

if num > 0:
  print("Esse número é maior que 0.")
elif num <0:
  print("Esse número é menor que 0.")
else:
  print("Esse número é igual a 0.")