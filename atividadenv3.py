# Classe mãe
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome} | CPF: {self.cpf} | Salário: R$ {self.salario:.2f}")

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R$ {self.salario:.2f}")


# Classe filha
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        # Reaproveita os atributos da classe mãe
        super().__init__(nome, cpf, salario)
        # Atributo exclusivo
        self.setor = setor

    # Sobrescrita do método exibir_dados para incluir o setor
    def exibir_dados(self):
        print(f"Nome: {self.nome} | CPF: {self.cpf} | Salário: R$ {self.salario:.2f} | Setor: {self.setor}")

    # Método exclusivo
    def receber_bonificacao(self):
        bonificacao = self.salario * 0.10
        self.salario += bonificacao
        print(f"🎉 Parabéns, {self.nome}! Você recebeu uma bonificação de 10% pelo desempenho no setor de {self.setor}.")
        print(f"Novo salário com bonificação: R$ {self.salario:.2f}")


# Demonstração de uso

# 1. Funcionário comum
func = Funcionario("Carlos Silva", "123.456.789-00", 3000.00)
func.exibir_dados()
func.aumentar_salario(5)  # Aumento de 5%
print("-" * 50)

# 2. Gerente
gerente = Gerente("Ana Souza", "987.654.321-11", 7000.00, "Tecnologia")
gerente.exibir_dados()
gerente.aumentar_salario(8)  # Aumento padrão de 8%
gerente.receber_bonificacao() # Bonificação exclusiva de 10%