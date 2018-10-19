#!/usr/bin/python3

class Conta():

    def __init__(self, titular, numero_conta,saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        if(self.saldo - saque < 0):
            print('Saldo insuficiente para realizar saque de R$ {}.\nSaldo atual: R${}'.format(saque,self.saldo))
        else:
            self.saldo -= saque

    def transferir(self, conta, transferencia):
        if(self.saldo - transferencia < 0):
            print('Saldo insuficiente para realizar transferencia de R$ {}.\nSaldo atual: R${}'.format(transferencia,self.saldo))
        else:
            self.saldo -= transferencia
            conta.depositar(transferencia)

    def __str__(self):
        return 'Titular: {} Saldo: {} Nro da Conta: {}'.format(self.titular,self.saldo,self.numero_conta)


class Poupanca(Conta):
    def __init__(self,titular,numero,saldo):
        super().__init__(titular,numero,saldo)
        self.juros = 1.005

    def render_juros(self):
        self.saldo *= self.juros
        return 'Saldo após rendimento de juros: R$ {}'.format(self.saldo)

conta = Poupanca('jonathas',102340,1000)
conta2 = Conta('lucas',102340)

print(conta.titular, conta.saldo, sep='\t')
conta.depositar(8000)
print(conta.titular, conta.saldo, sep='\t')
conta.sacar(3000)
print(conta.titular, conta.saldo, sep='\t')
print(conta2.titular, conta2.saldo, sep='\t')
conta.transferir(conta2,5000)
print(conta2.titular, conta2.saldo, sep='\t')
print(conta)
conta.render_juros()
print(conta)