# Exemplo de Coninue
while (
    True
):  # Essa linha define um loop infinito que continuará sendo executado até que uma condição dentro do loop cause a saída do loop.
    num = int(input("Digite um número:"))
    if num <= 0:  # verifica se o número inserido pelo usuário é menor ou igual a zero.
        continue  # Ele ignora o que tem no restante do laço e volta para o inicio
    print(num)
print("Fim")


"""
Aqui toda vez que o usuário digitar um n° maior que 0 ele vai imprimir na tela caso o n° 
for menor e = a 0 ele vai voltar ao inicio e pede para o usuario digitar um numero novamente 
e nao guarda ele 
"""
