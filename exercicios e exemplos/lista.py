#Isso é uma lista
lista = [1,2,3,4,5] #multiplicar todos os elemntos da lista

print(2*lista) #da errado

listam = []
listam = [x*2 for x in lista] #x vezes 2 para cada x em lista
print(listam)#assim multiplica valores na lista

listam2 = []

for e in lista: #para cada elemento em lista faça o seguinte:
    listam2.append(2*e) #é adicionado a listam2 elementos (lista) vezes 2
print(listam2) #Se não usar o append, resultado não sera o esperado, mostrou apenas o ultimo numero mult por 2



