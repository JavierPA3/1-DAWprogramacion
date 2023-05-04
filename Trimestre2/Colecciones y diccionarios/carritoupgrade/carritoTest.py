from carrito import Carrito
from elementos import Elemento

mi_carrito = Carrito()
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 2))
mi_carrito.agrega(Elemento("Canon EOS 2000D", 449, 1))
print(mi_carrito)
print(f"Hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f}  euros")

print("\nContinúa la compra...\n")
mi_carrito.agrega(Elemento("Samsung Galaxy Tab", 199, 3))
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 1))
print(mi_carrito)
print(f"Ahora hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f}  euros")
