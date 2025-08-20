"""
Desafio - Unidad 3: Practicas para el desarrollo de software
Autor: [Juan Diego Arevalo Quintero]
Descripcion:
  Programa que solicita 5 calificaciones, calcula el promedio y determina
  la situacion academica del estudiante:
    - Aprobado      : promedio >= 60
    - En recuperacion: 40 <= promedio <= 59
    - Reprobado     : promedio < 40
"""

# --- Configuracion ---
CANT_NOTAS = 5


def leer_calificaciones():
    """
    Solicita al usuario que ingrese 5 calificaciones y las devuelve en una lista.
    """
    notas = []
    for i in range(1, CANT_NOTAS + 1):
        nota = float(input(f"Ingrese la calificacion {i}: "))
        notas.append(nota)
    return notas


def calcular_promedio(notas):
    """
    Calcula el promedio de las calificaciones.
    """
    return sum(notas) / len(notas)


def clasificar(promedio):
    """
    Determina la situacion academica segun el promedio.
    """
    if promedio >= 60:
        return "Aprobado"
    elif 40 <= promedio <= 59:
        return "En recuperacion"
    else:
        return "Reprobado"


def main():
    print("=== EduTech Solutions - Calculadora de Promedio ===\n")
    notas = leer_calificaciones()
    promedio = calcular_promedio(notas)
    resultado = clasificar(promedio)

    print("\n--- Resumen ---")
    print("Calificaciones:", notas)
    print(f"Promedio final: {promedio:.2f}")
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
