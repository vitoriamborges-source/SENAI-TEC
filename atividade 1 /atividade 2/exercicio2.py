# Classe Mãe
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100

    def acelerar(self):
        if self.combustivel >= 5:
            self.combustivel -= 5
            print(f"O carro acelerou! Combustível restante: {self.combustivel}%")
        else:
            print("Sem combustível suficiente para acelerar!")

    def painel(self):
        print(f"Veículo: {self.marca} {self.modelo} | Combustível: {self.combustivel}%")


# Classe Filha
class CarroEletrico(Carro):
    def __init__(self, marca, modelo):
        # Inicializa marca e modelo na classe mãe
        super().__init__(marca, modelo)
        # Substitui a lógica de combustível tradicional por bateria
        self.combustivel = 0 
        self.bateria = 100

    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"O carro elétrico acelerou silenciosamente! Bateria restante: {self.bateria}%")
        else:
            print("Bateria insuficiente para acelerar! Por favor, recarregue.")

    def recarregar(self):
        self.bateria = 100
        print("Bateria totalmente recarregada (100%)!")

    def painel(self):
        print(f"Veículo Elétrico: {self.marca} {self.modelo} | Bateria: {self.bateria}%")


# --- DEMONSTRAÇÃO DE USO ---

# Instanciando o carro elétrico
meu_eletrico = CarroEletrico("Tesla", "Model 3")

# Exibindo o painel inicial
meu_eletrico.painel()

# Acelerando algumas vezes
meu_eletrico.acelerar()
meu_eletrico.acelerar()

# Verificando o painel atualizado
meu_eletrico.painel()

# Recarregando a bateria
meu_eletrico.recarregar()
meu_eletrico.painel()