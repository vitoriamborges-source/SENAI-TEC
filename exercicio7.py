class Bicicleta:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.velocidade = 0

    def pedalar(self):
        vel_anterior = self.velocidade
        if self.velocidade + 5 > 60:
            self.velocidade = 60
            print(f"[{self.modelo}] Pedalou! Velocidade atingiu o limite máximo de 60 km/h (Antes: {vel_anterior} km/h -> Depois: {self.velocidade} km/h)")
        else:
            self.velocidade += 5
            print(f"[{self.modelo}] Pedalou! Velocidade: {vel_anterior} km/h -> {self.velocidade} km/h")

    def freiar(self):
        vel_anterior = self.velocidade
        if self.velocidade == 0:
            print(f"[{self.modelo}] Freou, mas já está parada! Velocidade permaneceu em 0 km/h")
        else:
            self.velocidade = max(0, self.velocidade - 5)
            print(f"[{self.modelo}] Freou! Velocidade: {vel_anterior} km/h -> {self.velocidade} km/h")

    def radar_de_velocidade(self):
        print(f" radar ── Velocidade atual da bike ({self.modelo}): {self.velocidade} km/h")


# === Execução dos Testes ===

# Criação da bicicleta Caloi
minha_bike = Bicicleta(modelo="Caloi")

# Pedala 2 vezes
minha_bike.pedalar()
minha_bike.pedalar()

# Utiliza o radar de velocidade 1 vez
minha_bike.radar_de_velocidade()

# Freia 3 vezes
minha_bike.freiar()
minha_bike.freiar()
minha_bike.freiar()