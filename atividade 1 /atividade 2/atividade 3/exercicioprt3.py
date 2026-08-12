class ItemBiblioteca:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False


class Livro(ItemBiblioteca):
    def __init__(self, titulo, codigo, autor, num_paginas):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"'{item.titulo}' foi emprestado para {self.nome}.")
        else:
            print(f"Ops! '{item.titulo}' não está disponível.")

    def devolver_item(self, item):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"'{item.titulo}' foi devolvido por {self.nome}.")
        else:
            print(f"{self.nome} não está com o item '{item.titulo}'.")

    def ver_historico(self):
        print(f"\nItens com {self.nome}:")
        if not self.itens_emprestados:
            print("- Nenhum item no momento.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo} (Cód: {item.codigo})")


# --- Testando tudo na prática ---

# 1. Criando livros
l1 = Livro("O Hobbit", 101, "J.R.R. Tolkien", 310)
l2 = Livro("1984", 102, "George Orwell", 328)

# 2. Criando usuários
usr1 = Usuario("Lucas")
usr2 = Usuario("Mariana")

# 3. Empréstimo
usr1.pegar_item(l1)
usr1.pegar_item(l2)
usr1.ver_historico()

# 4. Tentando pegar livro indisponível
usr2.pegar_item(l1)

# 5. Devolução
usr1.devolver_item(l1)
usr1.ver_historico()

# 6. Agora o outro usuário consegue pegar
usr2.pegar_item(l1)
usr2.ver_historico()