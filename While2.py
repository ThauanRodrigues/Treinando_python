continua = "s"
soma = 0

while continua == "s":  # inicio do loop
    num = float(input("Digite um número:"))
    soma += num  # adiciona o valor de num à variável soma. A cada iteração do loop, o valor digitado pelo usuário será adicionado ao valor atual de soma.
    continua = input(
        "Deseja continuar? (s/n):"
    )  # caso o usuário digite s, será perguntado o numero dnv
print(f"Fim do programa, a soma total é: {soma}")
