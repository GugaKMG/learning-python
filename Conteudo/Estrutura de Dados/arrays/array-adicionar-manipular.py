from array import * #import array as arr

primeiro = array('i', [6,12]) #se usar o import acima, a criação de arrays fica assim: primeiro = arr.array('data type', value list)

print("Por enquanto, na posição 1 tem esse valor {}".format(primeiro[1])) #12
print("Por enquanto, na posição 0 tem esse valor {}".format(primeiro[0])) #6

primeiro.append(5) # adiciona um elemento

primeiro.extend([1,5,2,12]) #adiciona varios valores
                   #valor
primeiro.insert(3, 8)
            #posição onde se quer colocar o valor

print("Este array tem {} elementos".format(len(primeiro))) 
      #len mostra o tamanho da lista de valores

print("Este é o array agora: {}".format(primeiro))

primeiro.reverse()
print(primeiro)

print(primeiro.itemsize)

