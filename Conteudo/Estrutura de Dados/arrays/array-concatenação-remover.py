import array as arr

concat = arr.array('i', [1,5,3])
concat2 = arr.array('i', [2,4,8])
concatenado = arr.array('i')

concatenado = concat + concat2 #concat 2 irá para o final de concat
#Se concat2 tivesse sido o primeiro, concat ficaria no final
print("resultado da concatenação: {}".format(concatenado))

print(concatenado.pop(4)) #ele retorna o valor, se não colocar em um print não irá aparecer na tela

print(concatenado)

concatenado.remove(1)# este apenas remove

print(concatenado)
