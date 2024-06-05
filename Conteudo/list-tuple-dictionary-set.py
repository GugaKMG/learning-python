lista = []
#list

lista.append(5)
lista.append(45) #O pop não ira mostrar o ultimo item da lista
#adicionando valores na lista
                                                 #lists são mais usadas em banco de dados, arrays e melhor em JSON format, pois são parecidos com os arrays
lista.pop()
print("\nlista:", lista, "\n")

n = set()
#set
                                                 #Set é melhor em encontrar elementos unicos e join operations
n.add(7)
n.add(99)
#Adicionando valores na set

print("Na set tem o 7 e o 99", n, "\n")

n.remove(99)
print("Agora so tem o 7", n, "\n")

tup = (n) #no tuple o valor tem que estar entre os parenteses na hora de cria-lo e so pode conter um valor que ja esxite.
tup2 = tuple[int | str] = ("macaco", 5, 8, 10) 
                                                 #tuples são mais usados em pareteses check e colocar algo no banco de dados
                                                 #via SQL querry. Ex. do site: (1.’sravan’, 34).(2.’geek’, 35)
print("Tuple:", tup)
print("Teste do Tuple 2:", tup2)

dictionary = {}                                  #Melhor para fazer data frame com lists e JSON
#Dictionary

#adicionando valores               Note que cada um tem seu jeito de colocar e retirar valores.
dictionary[6] = "seis"
dictionary[9] = "nove"
print("Dictionary:", dictionary)

del dictionary[6]
print("Agora:", dictionary)