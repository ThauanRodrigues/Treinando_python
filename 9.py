'''
Faça um programa que receba as medidas dos 3 lados de um triangulo e diga se 
ele é equilatero, isosceles ou escaleno
'''
# Equilatero - Todos os lados iguais
# Isosceles - Possui dois lados iguais
# Escaleno - Todos os lado diferentes

lado1 = float(input("Digite o lado 1:"))
lado2 = float(input("Digite o lado 2:"))
lado3 = float(input("Digite o lado 3:"))

if (lado1 == lado2 and lado2 == lado3) :
    print("Esse triangulo é Equilatero!")
elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("Esse triangulo é Isosceles!")
else:
    print("Esse triangulo é Escaleno!")