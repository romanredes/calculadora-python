# calculadora.py
# Versión 1.2 - Operaciones: Suma, Resta y Multiplicación

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def main():
    print("Calculadora - Versión 1.2 (Suma, Resta y Multiplicación)")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")

    opcion = input("Elige una opción (1/2/3): ")

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
    elif opcion == "3":
        print(f"Resultado de la multiplicación: {multiplicar(a, b)}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
