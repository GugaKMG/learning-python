s = input("qual o seu genero? Use as letras f ou m.\n")

def main():
    if(s == "m" or s == "M"):
        print("Masculino\n")
    elif(s == "f" or s == "F"):
        print("Feminino.\n")
    else:
        print("Genero Invalido.\n")

if __name__ == "__main__":
    main()