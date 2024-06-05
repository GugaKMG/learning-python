import random

print("\n----Adivinhe o numero----\n")
print("A maquina irá escolher um numero de zero a cinco e voce devera adivinhar qual é\n")

numusu = int(input("Digite o numero: \n"))
numsorteio = random.randint(0,5)

if numusu == numsorteio:
    print("A maquina digitou o mesmo numero que o seu ({}), voce venceu.".format(numsorteio))
else:
    print("A maquina digitou um numero diferente, voce perdeu.")
    print("Esse foi o numero digitado pela maquina: {}".format(numsorteio))