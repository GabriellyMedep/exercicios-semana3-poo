# Exercícios Modelando um Sistema
"""1. O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
● Cada conta corrente pode ter um ou mais clientes como
titular.
● O banco controla apenas o nome, o telefone e a renda
mensal de cada cliente.
● A conta corrente apresenta um saldo e uma lista de
operações de saques e depósitos.
● Quando a cliente fizer um saque, diminuiremos o saldo da
conta corrente. Quando ela fizer um depósito,
aumentaremos o saldo.
● Clientes mulheres possuem em suas contas um cheque
especial de valor igual à sua renda mensal, ou seja, elas
podem sacar valores que deixam a sua conta com valor
negativo até renda_mensal.
● Clientes homens por enquanto não têm direito a cheque
especial.
Para modelar seu sistema, utilize obrigatoriamente os conceitos
"classe", "herança", "propriedades", "encapsulamento" e "classe
abstrata"."""

from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.__renda_mensal = renda_mensal

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Renda Mensal: {self.renda_mensal:.2f}"

class Conta(ABC):
    def __init__(self, clientes):
        self.clientes = clientes
        self.__saldo = 0
        self.operacoes = []

    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.operacoes.append(f"Depósito de R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    @abstractmethod
    def saque(self, valor):
        pass

class ContaMulher(Conta):
    def saque(self, valor):
        if valor > 0:
            limite = self.clientes[0].renda_mensal
            if self._Conta__saldo - valor >= -limite:
                self._Conta__saldo -= valor
                self.operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido para saque.")

class ContaHomem(Conta):
    def saque(self, valor):
        if valor > 0:
            if self._Conta__saldo - valor >= 0:
                self._Conta__saldo -= valor
                self.operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido para saque.")


cliente1 = Cliente('Maria', '99999-9999', 6000)
cliente2 = Cliente('João', '88888-8888', 5000)

conta1 = ContaMulher([cliente1])
conta2 = ContaHomem([cliente2])

conta1.deposito(2000)
conta1.saque(500)

conta2.deposito(3000)
conta2.saque(5000)
conta2.saque(500)

print(cliente1)
for operacao in conta1.operacoes:
     print(operacao)

print("\n")

print(cliente2)
for operacao in conta2.operacoes:
     print(operacao)

def get_balance(self):
        return self.__saldo

print(f"Saldo da Conta de Maria: R$ {conta1.saldo:.2f}")
print(f"Saldo da Conta de João: R$ {conta2.saldo:.2f}")
