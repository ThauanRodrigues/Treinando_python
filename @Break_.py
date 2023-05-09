# Break e Continue P41

# Exemplo de Break
while (
    True
):  # Essa linha define um loop infinito que continuará sendo executado até que uma condição dentro do loop cause a saída do loop.
    num = int(input("Digite um número:"))
    if num <= 0:  # verifica se o número inserido pelo usuário é menor ou igual a zero.
        break  # Caso o n° for menor que 0 o loop é interropido
print("Fim")

"""
Diferença entre Break e Continue
Break - ele encera o laço e continua o programa
Continue - ele ignora o que tem no restante do laço e volta para o inicio do laço
"""
