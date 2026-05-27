alunos = []

# Função para cadastrar aluno
def cadastrar():
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    alunos.append([nome, nota])

    print("Aluno cadastrado com sucesso!")

# Função para listar alunos
def listar():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")

    else:
        print("\nLISTA DE ALUNOS")
        
        for aluno in alunos:
            print("Nome:", aluno[0], "- Nota:", aluno[1])

# Função para mostrar média
def media():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")

    else:
        soma = 0

        for aluno in alunos:
            soma += aluno[1]

        media_final = soma / len(alunos)

        print("Média da turma:", media_final)

        if media_final >= 6:
            print("Turma aprovada!")

        else:
            print("Turma reprovada!")

# Menu principal
opcao = 0

while opcao != 4:

    print("\n=== MENU ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Ver média da turma")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        listar()

    elif opcao == 3:
        media()

    elif opcao == 4:
        print("Sistema encerrado.")

    else:
        print("Opção inválida!")