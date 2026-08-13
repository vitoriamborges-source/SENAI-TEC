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
        if item.emprestar():
            self.itens_emprestados.append(item)
            print(f"{self.nome} pegou '{item.titulo}' emprestado.")
        else:
            print(f"Não deu! '{item.titulo}' já está emprestado.")

    def devolver_item(self, item):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"{self.nome} devolveu '{item.titulo}'.")
        else:
            print(f"{self.nome} nem está com o livro '{item.titulo}'.")

    def ver_historico(self):
        print(f"\n[Livros com {self.nome}]")
        if not self.itens_emprestados:
            print("Nenhum livro no momento.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo} (cód: {item.codigo})")


# Testando a lógica
livro1 = Livro("1984", 101, "George Orwell", 328)
livro2 = Livro("Dom Casmurro", 102, "Machado de Assis", 200)

user = Usuario("Ana")

# Pegando livros
user.pegar_item(livro1)
user.pegar_item(livro2)
user.ver_historico()

# Tentando pegar um que já foi emprestado
user2 = Usuario("Carlos")
user2.pegar_item(livro1)

# Devolvendo
user.devolver_item(livro1)
user.ver_historico()