velo = int(input("Digite a velocidade que o carro estava: \n"))

if velo > 80:
    print("Você foi mutado, tera que pagar R${}\n".format((velo-80)*7))   #PRA DEIXAR DE SER MACACO, VELOCIDADE MENOS 80 VEZES 7, EX: 87-80=7*7-VALOR DA MULTA. 
else:
    print("Voce esta dentro do limite de velocidade.\n")