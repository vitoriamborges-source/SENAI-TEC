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