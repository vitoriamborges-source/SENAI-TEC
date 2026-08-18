class Carro:
    def acelerar(self):
        return "O carro está acelerando."

class CarroEsportivo(Carro):
    pass

ferrari = CarroEsportivo()
print(ferrari.acelerar())  # Saída: O carro está acelerando.