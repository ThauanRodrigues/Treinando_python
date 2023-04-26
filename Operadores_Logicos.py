# Operadores Lógicos

# AND - TODAS AS EXPRESSÕS VERDADEIRAS
# OR - PELO MENOS 1 EXPRESSÃO VERDADEIRA
# OR - INVERTE A  EXPRESSÇAO

#EXEMPLO DE END 

sou = input("Digite:")
idade = int(input("Qual a sua idade?"))

if(sou == "homem" and idade >= 18):
    print("Você pode tirar a reservista")
else:
    print("Você não tem os requesitos básicos.")


#Exemplo de Or
'''
estado = input("Digite seu estado")
if (estado == "Paraiba" or estado =="Bahia") :
    print("Atende!")
else:
    print("Não atendemos a esse estado.")
'''


