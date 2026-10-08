nomes = []
nota1 = []
nota2 = []

def cadastrar():
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    
    nomes.append(nome)
    nota1.append(n1)
    nota2.append(n2)
    
    print(f"Aluno {nome} cadastrado com sucesso!")

def calcular_media(indice):
    return (nota1[indice] + nota2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)

    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"

    return "Reprovado"

def listar():
    if len(nomes) == 0:
        print("Nenhum aluno cadastrado.")
        return

    print(f"\n{'NOME':<16} {'NOTA 1':<7} {'NOTA 2':<7} {'MÉDIA':<8} {'SITUAÇÃO':<14}")

    for i in range(len(nomes)):
        print(f"{nomes[i]:<16} {nota1[i]:<7} {nota2[i]:<7} {calcular_media(i):<8} {situacao(i):<14}")

def menu():
    while True:
        print("\n1. - Cadastrar Estudante")
        print("2. Listar Estudante")
        print("0. - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "0":
             break
        else:
             print("Opção inválida. ")

menu()
