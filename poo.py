class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        elif self.media() >= 4:
            return "Recuperação"

        return "Reprovado"
    def descrever(self):
        return (f"{self.nome:<16} {self.nota1:<7} {self.nota2:<7} {self.media():<8.1f} {self.situacao():<14}")
    
    Estudantes = []

def cadastrar():
    nome = input("Nome do estudante: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
        
    Estudante.Estudantes.append(Estudante(nome, n1, n2))
    print("Estudante cadastrado com sucesso!")

def listar():
    if len(Estudante.Estudantes) == 0:
        print("Nenhum aluno cadastrado.")
        return

    print(f"\n{'NOME':<16} {'NOTA 1':<7} {'NOTA 2':<7} {'MÉDIA':<8} {'SITUAÇÃO':<14}")
    for estudante in Estudante.Estudantes:
        print(estudante.descrever())

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