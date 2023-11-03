class ContaBancaria:
    def __init__(self, numero, nome, tipo):
        self.status = False
        self.limite = 0
        self.ativar_conta = False
        self.desativar_conta = False
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo


    def sacar(self, saque):
        if self.status == True:
            if saque > 0 and saque <= self.saldo + self.limite:
                self.limite = self.saldo - (saque - self.limite)
                self.saldo = self.saldo - saque
                print(f"Seu saque de R${saque} foi concluído com sucesso.")
            elif saque > self.limite:
                print(f"Seu limite é de: R${self.limite}.")
            else:
                print("Você não possui saldo suficiente.")
        else:
            print("Conta desativada, impossível sacar.")

    def depositar(self, deposito):
        if self.status == True:
            if deposito > 0:
                self.saldo += deposito
                print(f"Foi realizado um depósito de R${deposito}. Seu Saldo atual é de R${self.saldo}")
            else:
                print("Valor inválido.")
        else:
            print("Conta desativada")

    def ativar(self):
        if self.ativar_conta == False:
            self.ativar_conta = True
            self.status = True
            print("Conta ativada com sucesso!")
        else:
            print("A conta já está ativada.")

    def desativar(self):
        if self.saldo > 0:
            print("Impossível desativar conta com saldo positivo.")
        elif self.status == True:
            self.ativar_conta = False
            self.status = False
            self.desativar_conta = True
            print("Conta desativada!")

    def verificar_saldo(self):
        print(f"O saldo de sua conta é de: R${self.saldo}\nLimite R$:{self.limite}")

    def ativar_limite(self, valor):
        self.limite = valor
        print(f"Seu crédito especial é de R$: {self.limite}")

    def desativar_limite(self):
        self.limite = 0
        print(f"Seu crédito especial é de R$: {self.limite}")
