Python
import random

# 1. Transformando GABARITO em GABARITOS com 3 provas diferentes
GABARITOS = [
    ["A", "B", "C", "D", "A"],  # Prova 1
    ["B", "B", "A", "C", "D"],  # Prova 2
    ["D", "C", "B", "A", "A"]   # Prova 3
]


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        # Transformado self.nota em uma lista para histórico
        self.historico_notas = []

    def fazer_prova(self, respostas, gabarito):
        """Avalia a prova comparando com o gabarito fornecido e salva a nota no histórico."""
        nota = 0
        for resp_aluno, resp_correta in zip(respostas, gabarito):
            if resp_aluno.upper() == resp_correta.upper():
                nota += 2  # Supondo 5 questões valendo 2 pontos cada (Total = 10)

        # Adiciona a nota ao histórico em vez de sobrescrever
        self.historico_notas.append(nota)
        print(f"{self.nome} fez uma prova e tirou a nota: {nota}")

    def calcular_media(self):
        """Percorre o histórico de notas e retorna a média aritmética."""
        if not self.historico_notas:
            return 0.0

        soma = sum(self.historico_notas)
        media = soma / len(self.historico_notas)
        return media

    def ver_boletim(self):
        """Exibe o nome do aluno, histórico de notas, média final e situação."""
        media = self.calcular_media()
        situacao = "Aprovado" if media >= 6.0 else "Reprovado"

        print(f"\n================ BOLETIM DE {self.nome.upper()} ================")
        print(f"Histórico de Notas : {self.historico_notas}")
        print(f"Média Final        : {media:.2f}")
        print(f"Situação           : {situacao}")
        print("=" * (31 + len(self.nome)))