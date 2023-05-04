from CuentaCorriente import CuentaCorriente

cuenta1 = CuentaCorriente()
cuenta2 = CuentaCorriente(1500)
cuenta3 = CuentaCorriente(6000)

cuenta1.ingreso(2000)
cuenta1.cargo(600)
cuenta3.ingreso(75)
cuenta1.cargo(55)
cuenta2.transferencia(cuenta1, 100)
cuenta1.transferencia(cuenta3, 250)
cuenta3.transferencia(cuenta1, 22)
print(cuenta1.movimientos())
cuenta1.pass_to_file()
