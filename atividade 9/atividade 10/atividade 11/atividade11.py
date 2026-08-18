class CofreDigital:
    def __init__(self, titular: str, senha: str):
        self.titular = titular
        # Atributos privados iniciam com dois sublinhados (__):
        self.__senha = senha
        self.__saldo = 0.0

    def depositar(self, valor: float):
        """Deposita um valor no cofre caso seja maior que zero."""
        if valor > 0:
            self.__saldo += valor
            print(f"💰 [DEPÓSITO]: R$ {valor:.2f} depositado com sucesso no cofre de {self.titular}!")
        else:
            print("❌ Valor inválido para depósito.")

    def sacar(self, valor: float, senha_informada: str):
        """Realiza a validação da senha e do saldo antes de autorizar o saque."""
        # 1. Verifica se a senha informada corresponde à senha privada
        if senha_informada != self.__senha:
            print("🔒 Senha incorreta! Acesso negado.")
            return

        # 2. Verifica se há saldo suficiente
        if valor <= 0:
            print("❌ Valor de saque deve ser positivo.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print(f"✅ [SAQUE]: R$ {valor:.2f} retirado com sucesso! Saldo restante: R$ {self.__saldo:.2f}")
        else:
            print(f"⚠️ Saldo insuficiente! Saldo atual: R$ {self.__saldo:.2f}")

    def consultar_saldo(self, senha_informada: str):
        """Método auxiliar para consultar o saldo com validação de senha."""
        if senha_informada == self.__senha:
            print(f"📊 Saldo atual de {self.titular}: R$ {self.__saldo:.2f}")
        else:
            print("🔒 Senha incorreta! Acesso negado.")


# --- TESTANDO O COFRE E O ENCAPSULAMENTO ---

# Instanciando um CofreDigital com o titular e senha de 4 dígitos
meu_cofre = CofreDigital("Ana Silva", "1234")

print("--- 1. Operações Normais ---")
meu_cofre.depositar(500.0)
meu_cofre.sacar(150.0, "9999")  # Tenta sacar com senha errada
meu_cofre.sacar(150.0, "1234")  # Saca com a senha correta

print("\n--- 2. Tentando burlar o Encapsulamento ---")

# Tentativa de alterar o saldo diretamente:
meu_cofre.__saldo = 1000000.0
print("Tentando alterar meu_cofre.__saldo para 1.000.000...")

# Tentativa de alterar a senha diretamente:
meu_cofre.__senha = "0000"
print("Tentando alterar meu_cofre.__senha para '0000'...")

print("\n--- 3. Verificando se os atributos privados realmente mudaram ---")
# O saldo continuará sendo R$ 350.00 (500 - 150) e a senha continuará sendo "1234"
meu_cofre.consultar_saldo("1234")