"""
Faça um programa que declare uma variavel chamada continua e execute um laço while,
enquanto a variavel continua for == a "s", dentro do while, o usuario deve digitar um numero
e o usuario deve imprimir dobro do numero digitado.

E após essa impressão, perguntar se o usuario deseja continuar ou nao,
se o usuario digitar "s" , continua o laço,se digitar "n" o laÇõ se encerra.
"""
continua = "s"
while continua == "s":
    num = int(input("Digite um número:"))
    print(2 * num)
    continua = str(input("Deseja continuar? [s/n]"))
print("Programa finalizado!")
