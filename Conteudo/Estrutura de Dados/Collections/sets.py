# Sets são mutáveis, porém não permite duplicatas e não são ordenáveis.
mySet = {1, 2, 3, 4}

# Não irá adicionar, pois não perite repetidos.
mySet.add(2)

# Remove dados do Set.
mySet.remove(3)

# Tamanho do Set.
print(len(mySet))

# Iteração de Sets.
for itens in mySet:
    print(itens)

# Conversão de List para Set.
myList = (5, 6, 7, 8)
secondSet = set(myList)

print(secondSet)