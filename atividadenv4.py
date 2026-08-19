# Classe Mãe
class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True  # Inicia sempre como disponível

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O item '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O item '{self.titulo}' já está emprestado!")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O item '{self.titulo}' foi devolvido com sucesso.")
        else:
            print(f"O item '{self.titulo}' já está na biblioteca.")


# Classe Filha
class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        # Herda titulo e codigo da classe mãe (disponivel é definido como True no super)
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

    # Método utilitário para exibir os detalhes do livro
    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"[{self.codigo}] {self.titulo} - Autor: {self.autor} ({self.num_paginas} págs) | Status: {status}")


# Demonstração de uso
livro1 = Livro("O Hobbit", 101, "J.R.R. Tolkien", 310)

# Exibindo dados e testando o fluxo de empréstimo/devolução
livro1.exibir_informacoes()
livro1.emprestar()
livro1.exibir_informacoes()
livro1.emprestar()  # Tentativa de emprestar item indisponível
livro1.devolver()
livro1.exibir_informacoes()
# Estrutura base do acervo
class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
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
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas


# Nova Classe Usuario
class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item: ItemBiblioteca):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"Sucesso: {self.nome} pegou o item '{item.titulo}'.")
        else:
            print(f"Erro: O item '{item.titulo}' não está disponível para empréstimo.")

    def devolver_item(self, item: ItemBiblioteca):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"Sucesso: {self.nome} devolveu o item '{item.titulo}'.")
        else:
            print(f"Erro: {self.nome} não possui o item '{item.titulo}' em sua posse.")

    def ver_historico(self):
        print(f"\n--- Itens em posse de {self.nome} ---")
        if not self.itens_emprestados:
            print("Nenhum item emprestado no momento.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo} [Código: {item.codigo}]")
        print("-" * 35)


# Demonstration do funcionamento
livro1 = Livro("Dom Quixote", 101, "Miguel de Cervantes", 863)
livro2 = Livro("1984", 102, "George Orwell", 328)

usuario1 = Usuario("Lucas")
usuario2 = Usuario("Mariana")

# Fluxo de empréstimo
usuario1.pegar_item(livro1)
usuario1.pegar_item(livro2)

# Tentativa de pegar livro indisponível
usuario2.pegar_item(livro1)

# Consulta de histórico
usuario1.ver_historico()

# Devolução e nova tentativa
usuario1.devolver_item(livro1)
usuario2.pegar_item(livro1)

# Históricos atualizados
usuario1.ver_historico()
usuario2.ver_historico()