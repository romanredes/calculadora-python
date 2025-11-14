# calculadora.py
# Versión 1.3 - Operaciones: Suma, Resta, Multiplicación y División

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

def main():
    print("Calculadora - Versión 1.3 (Suma, Resta, Multiplicación y División)")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1/2/3/4): ")

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: debes ingresar solo números válidos.")
        return

    try:
        if opcion == "1":
            print(f"Resultado de la suma: {sumar(a, b)}")
        elif opcion == "2":
            print(f"Resultado de la resta: {restar(a, b)}")
        elif opcion == "3":
            print(f"Resultado de la multiplicación: {multiplicar(a, b)}")
        elif opcion == "4":
            resultado = dividir(a, b)
            print(f"Resultado de la división: {resultado}")
        else:
            print("Opción no válida.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
