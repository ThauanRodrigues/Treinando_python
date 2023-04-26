'''
Faça um programa que recebe três notas de 1 aluno
e diga se ele foi aprovado ou não.
Média
Acima de 7 Aprovado
Abaixo de 7 Reprovado
'''

n1 = float(input("Digite a sua 1° nota:"))
n2 = float(input("Digite sua 2° nota:"))
n3 = float(input("Digite sua3° nota:"))

media = (n1 + n2 + n3) / 2
print(f"Sua média é: {media}")

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado, Estude mais!")