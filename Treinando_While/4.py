"""
Faça um programa que inicie um laço de repetição qie execute
infinitamente.....
Dentro do while, declare uma variavel chamada n° 
que recebe uma entrada do usuario, o programa deve continuar solicitando até 
que o número seja 0, ai o laço será encerrado.
"""

while True:
    num = int(input("Digite um número:"))
    if num == 0:
        break

print("Fim")
