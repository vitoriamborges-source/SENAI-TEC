class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Todo objeto possui este método, que é chamado quando o objeto é convertido para string
    # Para os tipos de dados que utilizamos, como int, float, str, list, dict, etc., o método __str__ já está implementado.
    # Mas para os objetos que criamos, precisamos implementar este método para que possamos imprimir o objeto de forma legível.
    #ef __str__(self):
        #eturn f"Aluno: {self.nome}, Idade: {self.idade}"

gabriel = Aluno("Gabriel", 20)

# Sem definir o método __str__, o print(gabriel) iria imprimir o enreço de memória (RAM) do objeto, que não é muito legível.
# Com o método __str__ definido, o print(gabriel) imprime uma representação legível do objeto.
print(gabriel)