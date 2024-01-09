from arquivos.itens import Itens
import os

def titulo():
    print('''
    █░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █▀█ ▄▀█ █▀
    █▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▄▄ █▄█ █░▀░█ █▀▀ █▀▄ █▀█ ▄█\n\n''')

def menu():
    print('1 - Ver Lista')
    print('2 - Adicionar item')
    print('3 - Remover Item')
    print('4 - Sair\n')
    opcao = input("Digite uma opção: ")
    try:
        opcao = int(opcao)
        return opcao
    except:
        pass

def escolha(opcao):
    opcao = opcao
    match opcao:
        case 1:
            os.system('cls')
            titulo()
            Itens.ver_lista()
            main()
        case 2:
            os.system('cls')
            titulo()
            Itens.adicionar_item()
            main()
        case 3:
            os.system('cls')
            titulo()
            Itens.remover_item()
            main()
        case 4:
            os.system('cls')
            titulo()
            sair()
        case _:
            main()

def sair():
    print('Aplicação encerrada')

def main():
    os.system('cls')
    titulo()
    opcao = menu()
    escolha(opcao)

if __name__ == '__main__':
    main()