"""
Faça um programa que recebe um n° x digitado pelo usuário 
imprime todos os n° até 0 utilizandoo while 

"""

num = int(input("Digite um número:"))  # pedido um n°

while (
    num >= 0
):  # define um loop "enquanto a variavel num for maior ou = a 0, ele retorna"
    print(num)  # imprima
    num -= 1  # codição que apartir do numeor tira sempre -1
