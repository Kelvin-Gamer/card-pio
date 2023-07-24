class Cardapio:
    def __init__(self):
        self.itens = {}

    # Função para adicionar um item ao cardápio com o nome e preço informados
    def adicionar_item(self, nome, preco):
        self.itens[nome] = preco

    # Função para mostrar o cardápio atual, exibindo o nome e preço de cada item
    def mostrar_cardapio(self):
        print("----- Cardápio -----")
        for item, preco in self.itens.items():
            print(f"{item}: R${preco:.2f}")
        print("--------------------")


class Pedido:
    def __init__(self):
        self.pedido_atual = {}

    # Função para adicionar um item ao pedido atual, com o nome e a quantidade informados
    def adicionar_item(self, nome, quantidade):
        if nome in self.pedido_atual:
            self.pedido_atual[nome] += quantidade
        else:
            self.pedido_atual[nome] = quantidade

    # Função para calcular o total da conta com base nos itens do pedido atual e seus preços no cardápio
    def calcular_total(self, cardapio):
        total = 0
        for item, quantidade in self.pedido_atual.items():
            if item in cardapio.itens:
                total += cardapio.itens[item] * quantidade
        return total


def main():
    # Criação de uma instância do Cardápio
    cardapio = Cardapio()
    cardapio.adicionar_item("Hambúrguer", 10.50)
    cardapio.adicionar_item("Pizza", 25.00)
    cardapio.adicionar_item("Refrigerante", 5.00)

    # Criação de uma instância do Pedido
    pedido = Pedido()

    while True:
        print("\nOpções:")
        print("1 - Ver cardápio")
        print("2 - Adicionar item ao pedido")
        print("3 - Ver pedido atual")
        print("4 - Calcular total da conta")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            # Chama a função do Cardápio para mostrar o cardápio atual
            cardapio.mostrar_cardapio()
        elif opcao == 2:
            # Solicita ao usuário o nome e a quantidade do item para adicionar ao pedido
            item = input("Digite o nome do item que deseja adicionar ao pedido: ")
            quantidade = int(input("Digite a quantidade desejada: "))
            # Chama a função do Pedido para adicionar o item ao pedido atual
            pedido.adicionar_item(item, quantidade)
        elif opcao == 3:
            # Chama a função do Pedido para mostrar o pedido atual
            print("\n----- Pedido atual -----")
            for item, quantidade in pedido.pedido_atual.items():
                print(f"{item}: {quantidade}")
            print("------------------------")
        elif opcao == 4:
            # Chama a função do Pedido para calcular o total da conta com base no cardápio atual
            total = pedido.calcular_total(cardapio)
            print(f"Total da conta: R${total:.2f}")
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
