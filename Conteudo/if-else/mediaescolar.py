def main ():
    nota = int(input("Qual a sua nota?\n"))

    if(nota > 7):
        print("Aluno aprovado\n")
    elif (nota == 7): #assim faz um comentario em python
        print("Passou na risca kkkkk\n") 
    else:
        print("Aluno reprovado\n")

if __name__ == "__main__":
    main()