#Dictionarys não podem ter elementos duplicados, mas podem ser mudados.
#Esta é uma forma de fazer um dictionary:
dictionary = {
    "marca": "Lambo",
    "modelo": "Aventador",
    "ano": "2013"
}

#Esta é outra:
dictionary2 = dict(marca = "Lambo", modelo = "Aventador", ano = 2013)

#Printando os dois
print(dictionary)
print(dictionary2)

#Item específico
print(dictionary["marca"])

#Tamanho
print(len(dictionary))

#Revela o tipo de estrutura
print(type(dictionary))

#Iteração de dictionary
for x in dictionary:
    print(dictionary[x])