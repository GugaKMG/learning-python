num = float(input("Digite um número:\n"))

def main():
    if(num < 0):
        print("Este número é negativo.\n")
    elif(num == 0):
        print("Zero (0) não é nem negativo nem positivo.\n")
    else:
        print("Este número é positivo.\n")

if __name__ == "__main__":
    main()