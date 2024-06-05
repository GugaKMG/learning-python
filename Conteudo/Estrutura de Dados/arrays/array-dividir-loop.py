from array import *

loop = array('i', [4,1,6,3,5])
div = array('i', [3,1,6,8,9,5,6])
                # 1 2 3
print(div[0:3]) #pode-se contar como 1 2 3.
print(div[4:6]) #9 5 

for x in loop: #mostra todos os valores, apenas os valores
    print(x)
print("--------------")
for x in loop[0:2]:
    print(x)

    