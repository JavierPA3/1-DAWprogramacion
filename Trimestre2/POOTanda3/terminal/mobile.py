"""
12. Implementa la clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya no hace falta modificar
). Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar esto). El coste por
minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede cambiar.
Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada. A continuación se
proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer por pantalla. El
total tarificado debe aparecer con dos decimales.


Autor: Javier Postigo Arévalo
Fecha: 28/02/2023
"""
from Terminal import Terminal


class Mobile(Terminal):

    def __init__(self, number_of_account: str, tarifa: str):
        super().__init__(number_of_account)
        self.tarifa = tarifa
        self.euros_tarificado = 0

    def tarificado(self, seconds_call):
        rata = 0.06
        mono = 0.12
        bisonte = 0.30
        if self.tarifa.upper() == "RATA":
            self.euros_tarificado += (seconds_call/60) * rata
        elif self.tarifa.upper() == "MONO":
            self.euros_tarificado += (seconds_call/60) * mono
        elif self.tarifa.upper() == "BISONTE":
            self.euros_tarificado += (seconds_call/60) * bisonte

    def call(self, number_of_account: 'Terminal', seconds_call: int):
        if Terminal.check_if_number_is_registered(number_of_account.number_of_account):
            self.minutes_of_account += seconds_call
            number_of_account.minutes_of_account += seconds_call
            self.tarificado(seconds_call)
        else:
            return None

    def __str__(self):
        return f"No {self.account_full_number} - {self.minutes_of_account}s de conversación - tarificados " \
               f"{round(self.euros_tarificado, 3):.2f} euros."
