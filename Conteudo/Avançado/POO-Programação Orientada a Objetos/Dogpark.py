class CachorroParque:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        #tiramos o atributo raça

    def descricao(self):
        return f"{self.nome} é um {self.raca} de {self.idade} anos de idade"

    def speak(self,som):
        self.som = som
        return f"{self.nome} disse dessa forma algos {self.som}"
        
class Bulldog(CachorroParque):
    def speak(self, som="whof"):
        return super().speak(som)
        #O som se mantem inalteravel, mas a string inteira ficará como o original.
class Chiuaua(CachorroParque):
    def speak(self, som="au"):
        return f"{self.nome} disse {som}"

class Macaco(CachorroParque):
    def speak(self, som="CAVALO"):
        return f"{self.nome} disse {som}"
