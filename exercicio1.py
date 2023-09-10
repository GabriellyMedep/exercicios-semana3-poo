# Exercícios Classes e Objetos
"""1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe."""

class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False

    def acelera(self, incremento):
         if self.ligado:
            self.velocidade += incremento
            print(f"O {self.modelo} de cor {self.cor} acelerou para {self.velocidade} km/h.")

    def desacelera(self, decremento):
        if self.ligado:
            self.velocidade -= decremento
            print(f"O {self.modelo} de cor {self.cor} desacelerou para {self.velocidade} km/h.")
    
    def __str__(self):
        ligado_str = "ligado" if self.ligado == True else "desligado"
        return f"Carro {self.modelo} da cor {self.cor} está {ligado_str}, à velocidde de {self.velocidade} km/h."

# Instância da classe carro
meu_carro = Carro("cinza", "nissan")
print(meu_carro)

# Para o carro andar
meu_carro.liga() # Liga o carro
meu_carro.acelera(50) # Acelera para 50 km/h
meu_carro.acelera(100) # Acelera para 150 km/h
meu_carro.desacelera(50) # Desacelera para 100 km/h

# Para o carro parar
meu_carro.desacelera(100) # Desacelera para 0 km/h
print("Carro nissan de cor cinza está desligado, à velocidade de 0 km/h. ")

