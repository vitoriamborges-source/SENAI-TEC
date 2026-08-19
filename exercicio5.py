class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade: int) -> bool:
        """Reduz a quantidade do estoque caso haja unidades suficientes."""
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print(f"[ERRO] Estoque insuficiente para '{self.nome}'. Disponível: {self.estoque}")
            return False


class CarrinhoDeCompras:
    def __init__(self):
        # Inicia a lista vazia de produtos
        self.produtos = []

    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int):
        """Adiciona o produto e a quantidade ao carrinho se houver estoque suficiente."""
        if produto.estoque >= quantidade:
            # Adiciona como uma tupla (produto, quantidade)
            self.produtos.append((produto, quantidade))
            print(f"-> {quantidade}x '{produto.nome}' adicionado(s) ao carrinho!")
        else:
            print(f"[ERRO] Não foi possível adicionar '{produto.nome}'. Estoque insuficiente ({produto.estoque}).")

    def mostrar_carrinho(self):
        """Percorre e exibe todos os itens presentes no carrinho com o valor total."""
        print("\n================ SEU CARRINHO ================")
        
        if not self.produtos:
            print("O carrinho está vazio.")
            print("==============================================")
            return

        total_compra = 0.0

        for item, qtd in self.produtos:
            subtotal = item.preco * qtd
            total_compra += subtotal
            print(f"• {item.nome} | Qtd: {qtd} | R$ {item.preco:.2f} un. -> Subtotal: R$ {subtotal:.2f}")

        print("----------------------------------------------")
        print(f"TOTAL DA COMPRA: R$ {total_compra:.2f}")
        print("==============================================")

    def finalizar_compra(self):
        """Método extra: consolida a compra e reduz o estoque dos produtos."""
        if not self.produtos:
            print("O carrinho está vazio. Nada para finalizar.")
            return

        print("\n--- Finalizando Compra ---")
        for item, qtd in self.produtos:
            item.reduzir_estoque(qtd)
        
        self.produtos.clear()
        print("Compra realizada com sucesso e carrinho esvaziado!")