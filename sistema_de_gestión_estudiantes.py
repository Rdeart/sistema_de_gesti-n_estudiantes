def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")

    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("Error: edad inválida. Ingrese una edad válida.")
            else:
                break
        except ValueError:
            print("Error: debe ingresar un número entero.")

    while True:
        try:
            nota1 = float(input("Ingrese la primera nota del estudiante: "))
            if 0 <= nota1 <= 5:
                break
            else:
                print("Nota inválida. Debe estar entre 0 y 5.")
        except ValueError:
            print("Error: debe ingresar un número válido.")

    while True:
        try:
            nota2 = float(input("Ingrese la segunda nota del estudiante: "))
            if 0 <= nota2 <= 5:
                break
            else:
                print("Nota inválida. Debe estar entre 0 y 5.")
        except ValueError:
            print("Error: debe ingresar un número válido.")

    while True:
        try:
            nota3 = float(input("Ingrese la tercera nota del estudiante: "))
            if 0 <= nota3 <= 5:
                break
            else:
                print("Nota inválida. Debe estar entre 0 y 5.")
        except ValueError:
            print("Error: debe ingresar un número válido.")

    return nombre, edad, nota1, nota2, nota3


def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"


prom = 0
contador = 0
estudiantes = []

while True:
    print("\n====== SISTEMA DE GESTIÓN DE ESTUDIANTES ======")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        print("--- Registrar estudiante ---")
        nombre, edad, nota1, nota2, nota3 = registrar_estudiante()
        print("\n=== RESULTADO DEL ESTUDIANTE ===")
        promedio = calcular_promedio(nota1, nota2, nota3)
        resultado = evaluar_estado(promedio)

        estudiantes.append(
            {
                "Nombre": nombre,
                "Edad": edad,
                "Promedio": promedio,
                "Estado": resultado,
            }
        )

        prom += promedio
        contador += 1

        print(f"El promedio del estudiante {nombre} es: {promedio:.2f}")
        print(f"Estado académico: {resultado}")

    elif opcion == "2":
        print("\n====== LISTA DE ESTUDIANTES REGISTRADOS ======")
        if contador == 0:
            print("No hay estudiantes registrados.")
        else:
            for est in estudiantes:
                print(est)

    elif opcion == "3":
        print("\n====== RESUMEN FINAL ======")
        if contador > 0:
            print(f"Total de estudiantes registrados: {contador}")
            print(f"Promedio general del grupo: {prom / contador:.2f}")
        else:
            print("No hay estudiantes registrados.")
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
