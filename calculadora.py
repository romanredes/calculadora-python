# calculadora.py
# Versión 1.1 - Operaciones: Suma y Resta

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def main():
    print("Calculadora - Versión 1.1 (Suma y Resta)")
    print("1. Sumar")
    print("2. Restar")

    opcion = input("Elige una opción (1/2): ")

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: debes ingresar solo números válidos.")
        return

    if opcion == "1":
        print(f"Resultado de la suma: {sumar(a, b)}")
    elif opcion == "2":
        print(f"Resultado de la resta: {restar(a, b)}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
