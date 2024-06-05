nomes = ['Claudio', 'Rafael', 'Smzinho']

for n in nomes:
    print(n)

nome = str(input("Digite um nome: \n"))
#Mesmo n sendo igual, não interfere no resultado de cada um.
for n in nome: # Para(for) cada n(variavel) em(in) nome(variavel ou lista) faça:
    print(nome*2) 
    #Para cada letra de Joao, por exemplo, ele irá imprimir o nome duas vezes para cada letra. 
else:
    print("Fim dos loops.") #Else pode ser usado para que execute os comando ao loop acabar.

