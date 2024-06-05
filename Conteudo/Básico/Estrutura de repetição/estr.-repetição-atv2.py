usu = input("Diga seu nome de usuario:\n")
senha = input("Diga sua senha:\n")

while senha:
    if senha == usu:
        print("A senha não pode ser a mesma que o nome do usuario:\n")
        senha = input("Digite sua senha novamente:\n")
    else: 
        print("Bem-vindo!")
        break