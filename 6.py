'''
Faça um programa que recebe a idade do usuário e diga se 
ele já pode tirar a CNH ou não.
'''

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Você ja pode tirar Habilitação!")
else:
    print("Você é novo demais pra tirar Habilitação.")