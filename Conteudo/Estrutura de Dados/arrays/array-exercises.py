from array import *

integers = array('i', [3,1,4,5,2])

for x in integers:
    print(x)
print("------------")
print("Apenas os três primeiros numeros:\n")
for x in integers[0:3]: #Para acessar apenas os primeiros numeros e fazer como no exemplo anterior
    print(x)
print("------------")
print("Novo array:\n")
integers.append(14)
print(integers)

print("------------")
print("Invertendo o array: \n")
integers.reverse() #Use isto para quando precisar inverter um array.

print(integers.itemsize) #mostra o tamanho do array em bytes
