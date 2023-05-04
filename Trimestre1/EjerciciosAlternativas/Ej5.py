"""
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que
ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

Fecha: 15/10/2022

Autor: Javier Postigo
"""
print("Programa que lee la edad de dos personas y dice cual es mas joven.")

person_one = int(input("¿Cuántos años tiene la primera persona? "))
person_two = int(input("¿Cuántos años tiene la segunda persona? "))

if person_one > person_two:
    print(f"La primera persona ({person_one}) tiene más años que la segunda ({person_two}).")
elif person_one == person_two:
    print(f"Tienen la misma edad ({person_one}).")
else:
    print(f"La segunda persona ({person_two}) tiene más años que la primera ({person_one}).")
