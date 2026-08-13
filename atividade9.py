class Livro:
    # 1. Construtor: cria os atributos da classe
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # 2. Método especial para formatar a exibição quando usamos print()
    def __str__(self):
        return f"Livro: '{self.titulo}' por {self.autor} ({self.paginas} pgs)"

    # 3. Método para comparar a quantidade de páginas entre dois livros
    def comparar_tamanho(self, outro_livro):
        if self.paginas > outro_livro.paginas:
            print(f"O livro '{self.titulo}' tem mais páginas ({self.paginas} pgs) que '{outro_livro.titulo}' ({outro_livro.paginas} pgs).")
        elif self.paginas < outro_livro.paginas:
            print(f"O livro '{outro_livro.titulo}' tem mais páginas ({outro_livro.paginas} pgs) que '{self.titulo}' ({self.paginas} pgs).")
        else:
            print(f"Ambos os livros '{self.titulo}' e '{outro_livro.titulo}' têm o mesmo número de páginas ({self.paginas} pgs).")


# --- EXECUTANDO O CÓDIGO ---

# Instanciando 2 livros
livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 310)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 256)

# Testando o método __str__ usando print() direto nas variáveis
print(livro1)
print(livro2)

print("\n--- Comparação de Tamanho ---")
# Comparando os livros
livro1.comparar_tamanho(livro2)