# calculadora.py
# Versión 1.1 - Solo suma

def sumar(a, b):
    return a + b

def main():
    print("Calculadora - Versión 1.1 (Solo suma)")

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: debes ingresar solo números válidos.")
        return

    resultado = sumar(a, b)
    print(f"Resultado de la suma: {resultado}")

    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
