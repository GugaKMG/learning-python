num1 = float(input("Digite um número: \n"))
num2 = float(input("Digite outro: \n"))

def main ():
    if (num1 > num2):
        print(num1, "é maior que", num2)
    else:
        print(num2, "é maior que", num1)
    
if __name__ == "__main__":
    main()