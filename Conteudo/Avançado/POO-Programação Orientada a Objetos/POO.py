class Cachorro: 
    #atributo de class
    especie = "Canis familiaris"
#Função     #instance attributes   
    def __init__(self, nome, idade):
        self.nome = nome #Cria um atributo chamado nome designando para ele o valor dos parametros de nome.
        self.idade = idade #Cria um atributo chamado idade designando para ele o valor do parametro de idade.

    #Este é um metodo instance
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade." # Retorna uma string mostrando o nome e a idade do cachorro. 

    #Este é outro metodo instance
    def speak(self, som):
        return f"{self.nome} says {som}." #Retorna o nome do cachorro e o som que faz. 