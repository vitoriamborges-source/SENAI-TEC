class OrdemDeServico:
    # Atributos de classe (compartilhados por todas as instâncias)
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente: str, descricao: str):
        self.cliente = cliente
        self.descricao = descricao
        self.status = "Aberta"

        # Incrementa os contadores da classe
        OrdemDeServico.total_os_criadas += 1
        OrdemDeServico.os_abertas += 1

        # Atribui o número atual de total_os_criadas como ID único desta OS
        self.id_os = OrdemDeServico.total_os_criadas

    def finalizar_os(self):
        """Altera o status para Concluída e decrementa as OS abertas."""
        if self.status == "Aberta":
            self.status = "Concluída"
            OrdemDeServico.os_abertas -= 1
            print(f"✅ OS #{self.id_os} ({self.cliente}) foi finalizada!")
        else:
            print(f"⚠️ OS #{self.id_os} já estava concluída.")

    @classmethod
    def verificar_os_abertas(cls):
        """Método de classe para consultar a quantidade de OSs em aberto."""
        print(f"📋 Quantidade de ordens de serviço abertas no momento: {cls.os_abertas}")
        return cls.os_abertas


# --- EXECUTANDO O CÓDIGO ---

# 1. Instanciando 3 ordens de serviço
os1 = OrdemDeServico("Carlos Silva", "Troca de tela do celular")
os2 = OrdemDeServico("Maria Souza", "Formatação de notebook")
os3 = OrdemDeServico("João Pedro", "Manutenção em impressora")

print(f"OS 1 -> ID: {os1.id_os} | Cliente: {os1.cliente} | Status: {os1.status}")
print(f"OS 2 -> ID: {os2.id_os} | Cliente: {os2.cliente} | Status: {os2.status}")
print(f"OS 3 -> ID: {os3.id_os} | Cliente: {os3.cliente} | Status: {os3.status}\n")

# Verificando a quantidade inicial de ordens abertas (deve ser 3)
OrdemDeServico.verificar_os_abertas()

print("\n--- Concluindo uma OS ---")
# 2. Concluindo a primeira OS
os1.finalizar_os()

print("\n--- Verificação Final ---")
# 3. Verificando novamente quantas ordens estão abertas (deve ser 2)
OrdemDeServico.verificar_os_abertas()