# Classe Mãe
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz um som genérico.")


# Classes Filhas
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Canino")
        self.raca = raca

    def fazer_som(self):
        print(f"O cachorro {self.nome} ({self.raca}) faz: Au Au!")


class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Felino")
        self.raca = raca

    def fazer_som(self):
        print(f"O gato {self.nome} ({self.raca}) faz: Miau!")


class Vaca(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Bovino")
        self.raca = raca

    def fazer_som(self):
        print(f"A vaca {self.nome} ({self.raca}) faz: Muuu!")


# --- DEMONSTRAÇÃO DE USO E POLIMORFISMO ---

# Instanciando um objeto de cada classe
rex = Cachorro(nome="Rex", raca="Pastor Alemão")
felix = Gato(nome="Felix", raca="Siamês")
mimosa = Vaca(nome="Mimosa", raca="Holandesa")

# Lista de animais para demonstrar o Polimorfismo
animais = [rex, felix, mimosa]

# Chamando o mesmo método para objetos de classes diferentes
for animal in animais:
    animal.fazer_som()