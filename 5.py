'''
Faça um programa que recebe a altura e o peso do usuario 
e calcule O seu IMC
'''
altura = float(input("Digite sua altura:"))
peso = float(input("Digite o seu peso:"))

Imc = peso / (altura**2)
print(f"O seu IMC é de: {Imc}")