"""
Test de la clase BankAccount
"""

from BankAccount import BankAccount

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)