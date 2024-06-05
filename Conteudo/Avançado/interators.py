class Teste:
    def __init__(self,limit):
        self.limit = limit

#Cria um o bjeto iterator que vai ser chamado toda vez que uma iteration for inicializada.
    def __iter__(self):
        self.x = 10
        return self
# Para mover para o proximo elemento nós usamos __next__ no Python 3
    def __next__(self):
        #Armazenar o valor atual
        x = self.x

        #Faz a iteração parar quando chegar no limite.
        if x > self.limit:
            raise StopIteration

        #Senão incrementa um e retorna o valor antigo
        self.x = x + 1
        return x 

#Vai emprimir na tela numeros de 10 a 15
for i in Teste(15):
    print(i)

#Não irá emprimir nada
for i in Teste(5):
    print(i)