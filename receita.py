import os


def registrar():
    nome = input("Nome da receita:")
    ingredientes = input("Ingredientes: ")
    modo_de_preparo = input("Modo de preparo: ")
    with open("receitas.txt", "a") as arquivo:
        arquivo.write(f" Nome da receita: {nome} \n Ingredientes: {ingredientes} \n Modo de Preparo: {modo_de_preparo} \n ******************************************\n")


def consultar():
    nome = input("Digite o nome da receita que deseja consultar:").strip()
    with open("receitas.txt", "r") as arquivo:
        encontrada = False
        for linha in arquivo:
            if f"Nome da receita: {nome}" in linha:
                encontrada = True
                print(linha)
                linha = next(arquivo) 
                while linha.strip() != "******************************************":
                    print(linha)
                    linha = next(arquivo) 
                break  
        if not encontrada:
            print("Receita não encontrada.")

def listar():
    with open("receitas.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha)

def limpar():
    try: 
        os.remove("receitas.txt")
        print("Arquivo limpo com sucesso")
    except:
        print("Arquivo não encontrado")


def menu():
    while True:
        print("\n*** Menu ***")
        print("1 - Criar Receita")
        print("2 - Consultar Receita")
        print("3 - Listar Receitas")
        print("4 - Limpar Arquivo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar()
        elif opcao == "2":
            consultar()
        elif opcao == "3":
            listar()
        elif opcao == "4":
            limpar()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()