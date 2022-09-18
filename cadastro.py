nome = []
idade = []
curso = []
localidade = []

repetir = "S"

while repetir == "S":

    nome.append((input("digite seu nome: ")))
    idade.append(int(input("digite sua idade: ")))
    curso.append(input("digite seu curso:"))   
    localidade.append(input("informe sua cidade: "))
    repetir = input("Quer fazer novamente digite S: ").upper()


for i in range(len(nome)):
    print("\nNome.. ",nome[i])
    print("idade.. ",idade[i])
    print("curso.. ",curso[i])
    print("cidade.. ",localidade[i])