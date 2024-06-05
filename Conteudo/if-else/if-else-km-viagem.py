km = int(input("Quantos kilometros dara essa viagem?\n"))

if km < 200:
    km = km * 0.50
    print("Sua viagem custara {}".format(km))
else:
    km = km * 0.45
    print("Sua viagem custara {}".format(km))