class Itens:

    lista = []

    def __init__(self, nome, quantidade):
        self._nome = nome
        self._quantidade = quantidade
    
    def __str__(self):
        return (f'{self._nome} | {self._quantidade}')
    
    def adicionar_item():
        nome_do_item = input('Digite o nome do item: ')
        quantidade_do_item = int(input('Digite a quantidade de itens: '))
        item = Itens(nome_do_item, quantidade_do_item)
        Itens.lista.append(item)
        input('Item adicionado com sucesso. Pressione ENTER para continuar...')

    @classmethod
    def ver_lista(cls):
        print(f'{"Produto".ljust(20)} | {"Quantidade".ljust(20)}')
        for item in cls.lista:
            print(f'{item._nome.ljust(20)} | {str(item._quantidade).ljust(20)}')
        input('\nPressione ENTER para retornar ao menu...')
    
    @classmethod
    def remover_item(cls):
        print(f'{"Índice".ljust(10)} | {"Produto".ljust(20)} | {"Quantidade".ljust(20)}')
        indice = 0
        for item in cls.lista:
            print(f'{str(indice).ljust(10)} | {item._nome.ljust(20)} | {str(item._quantidade).ljust(20)}')
            indice += 1
        excluir = input('Digite o índice do item que deseja deletar: ')
        try:
            excluir = int(excluir)
            if 0 <= excluir < len(Itens.lista):
                del Itens.lista[excluir]
                input('Ítem excluído com sucesso. Pressione ENTER para retornar ao menu...')
            else:
                input('Opção inválida. Pressione ENTER para retornar ao menu...')
        except:
            input('Opção inválida. Pressione ENTER para retornar ao menu...')