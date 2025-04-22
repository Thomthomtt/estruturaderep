nome=input("Qual o seu nome? ")
idade=int(input("Qual a sua idade? "))
altura=float(input("Qual a sua altura? "))
estudante=(input("Você é um estudante? S/N "))
if estudante=='s':
    estudante="você é um estudante"
elif estudante=='n':
    estudante="você não é um estudante"
else:
    estudante="Caracter Invalido"
print(f"Seu nome é {nome}, você tem {idade} anos, tem {altura} de altura e... \n{estudante}!")

