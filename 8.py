'''
Faça um programa que calcule o desconto de um produto 
de acordo com a forma de pagamento escolhido pelo cliente.

A vista 10%
Cartão 5% 
Parcelado Normal
'''
preco = float(input("Informe o valor da comprar:"))

print("1. Á vista\n2. Com cartão\n3. Parcelado")
opcao = int(input("Escolha a forma de pagamento"))

if (opcao == 1):
    calculo = opcao * 0.90
    print(f"O Preço final: {calculo}")
elif (opcao == 2):
    calculo = opcao *0.95
    print(f"O Preço final: {calculo}")
elif (opcao == 3):
    print(f"O Preço final: {preco}")
else:
    print("Opção invalida.")