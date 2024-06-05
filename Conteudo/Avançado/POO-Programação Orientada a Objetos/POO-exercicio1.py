class Carro:
    def __init__(self, cor, quilometragem):
        self.cor = cor
        self.quilometragem = quilometragem

    def descricao(self):
        return f"Esse carro tem a cor {self.cor} e {self.quilometragem} de km andados."

#Outra solução no IDLE:
#Faça o codigo acima sem o def descricao
#No IDLE:

#azulc = Carro(color="azul", quilometragem=20,000)
#verc = Carro(color="vermelho", quilometragem=30,000)

#for car in (azulc, verc):
#    print(f"O carro {carro.cor} tem {carro.quilometragem} km andados.")
#Isso resolve o problema orignal que pedia para que a cor seja uma string enquanto os km sejam um integer.