class Aplicativo:
    def __init__(self, nome: str, consumo_bateria: int = 100):
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, modelo: str, bateria: int = 100):
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"[{self.modelo}] Celular ligado.")

    def desligar(self):
        self.ligado = False
        print(f"[{self.modelo}] Celular desligado.")

    def executar_app(self, app: Aplicativo):
        # 1. Verifica se o celular está ligado
        if not self.ligado:
            print(f"Erro: Não é possível executar '{app.nome}'. O celular está desligado.")
            return

        # 2. Verifica se a bateria é suficiente
        if self.bateria < app.consumo_bateria:
            print(f"Erro: Bateria insuficiente ({self.bateria}%) para executar '{app.nome}' (requer {app.consumo_bateria}%).")
            return

        # 3. Subtrai o consumo e executa
        self.bateria -= app.consumo_bateria
        print(f"Executando '{app.nome}'... Bateria restante: {self.bateria}%")


# === Execução do Exemplo ===

# Criação de dois aplicativos com consumos diferentes
app1 = Aplicativo(nome="Rede Social", consumo_bateria=25)
app2 = Aplicativo(nome="Jogo 3D", consumo_bateria=60)

# Criação do objeto Celular
meu_celular = Celular(modelo="Smartphone X", bateria=100)

# Liga o aparelho e executa os aplicativos
meu_celular.ligar()
meu_celular.executar_app(app1)
meu_celular.executar_app(app2)