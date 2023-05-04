
import sys

# Verificar si se han proporcionado los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python mi_script.py arg1 arg2")
    sys.exit(1)

# Obtener los argumentos pasados por línea de comandos
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Realizar la tarea con los argumentos
print("El valor del primer argumento es:", arg1)
print("El valor del segundo argumento es:", arg2)