lista = []
lista.append(int(input("Digite um numero de 0 a 10: \n")))

for n in lista:
    if n < 0 or n > 10:
        print("Valor inválido, digite um numero de 0 a 10:\n")
        lista.append(int(input()))
    else:
        print("Valor válido.\n")
else:
    print("fim do programa.\n")