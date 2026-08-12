import random

class PetVirtual:
    def __init__(self, nome: str, fome: int = 5, felicidade: int = 5):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade

    def _aplicar_bonus_felicidade_aleatoria(self):
        # Diminui a felicidade por um valor aleatório entre 0 e 2
        perda_aleatoria = random.randint(0, 2)
        self.felicidade = max(0, self.felicidade - perda_aleatoria)
        if perda_aleatoria > 0:
            print(f"   (A felicidade diminuiu em {perda_aleatoria} aleatoriamente!)")

    def alimentar(self):
        print(f"\n Alimentando {self.nome}...")
        if self.fome == 0:
            print(f"{self.nome} disse: Ele está cheio!")
        else:
            self.fome = max(0, self.fome - 2)
            print(f"Nome: {self.nome} | Fome atual: {self.fome}")
        
        self._aplicar_bonus_felicidade_aleatoria()

    def brincar(self):
        print(f"\n Brincando com {self.nome}...")
        self.felicidade += 2
        self.fome += 1
        print(f"Nome: {self.nome} | Felicidade: {self.felicidade} | Fome: {self.fome}")
        
        self._aplicar_bonus_felicidade_aleatoria()

    def status(self):
        print(f"\n=== STATUS DE {self.nome.upper()} ===")
        print(f"Nome: {self.nome} | Felicidade: {self.felicidade} | Fome: {self.fome}")
        
        self._aplicar_bonus_felicidade_aleatoria()


# === Execução do Script ===

# 1. Crie um PetVirtual
meu_pet = PetVirtual(nome="Tamagotchi")

# 2. Mostre o status
meu_pet.status()

# 3. Brinque 2 vezes
meu_pet.brincar()
meu_pet.brincar()

# 4. Alimente 3 vezes
meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.alimentar()

# 5. Mostre o status final
meu_pet.status()