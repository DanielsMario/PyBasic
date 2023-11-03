from main import *

conta1 = ContaBancaria(123, "Danyel", "Corrente")

conta1.ativar()
conta1.depositar(1000)
conta1.sacar(500)
conta1.verificar_saldo()
conta1.desativar()
