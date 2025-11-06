# calculadora.py
# Versión 1.0 - Operación: Suma

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculadora - Versión 1.0 (Suma)")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    resultado = sumar(a, b)
    print(f"Resultado: {resultado}")
