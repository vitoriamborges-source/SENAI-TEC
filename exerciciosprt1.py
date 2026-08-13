# Classe Mãe
class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O item '{self.titulo}' (Código: {self.codigo}) foi emprestado com sucesso.")
        else:
            print(f"O item '{self.titulo}' não está disponível para empréstimo no momento.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O item '{self.titulo}' (Código: {self.codigo}) foi devolvido com sucesso.")
        else:
            print(f"O item '{self.titulo}' já consta como disponível na biblioteca.")


# Classe Filha
class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Livro: {self.titulo} | Autor: {self.autor} | Páginas: {self.num_paginas} | Código: {self.codigo} | Status: {status}")


# --- DEMONSTRAÇÃO DE USO ---

# Instanciando um livro
livro1 = Livro("Dom Casmurro", 101, "Machado de Assis", 256)

# Exibindo informações iniciais
livro1.exibir_informacoes()

# Realizando o empréstimo
livro1.emprestar()
livro1.exibir_informacoes()

# Tentando emprestar novamente (deve informar indisponibilidade)
livro1.emprestar()

# Devolvendo o livro
livro1.devolver()
livro1.exibir_informacoes()