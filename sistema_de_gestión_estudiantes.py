def registro_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        edad = int(input("Ingrese la edad del estudiante: "))
        if edad < 0:
            print("Error: edad inválida. Ingrese una edad válida.")
        else:
            print(f"Estudiante registrado: {nombre}, Edad: {edad}")
            break
    while True:
        nota1 = float(input("Ingrese la primera nota del estudiante: "))
        if nota1 < 0 or nota1 > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
        else:
            print(f"Primera nota registrada: {nota1}")
            break
    while True:
        nota2 = float(input("Ingrese la segunda nota del estudiante: "))
        if nota2 < 0 or nota2 > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
        else:
            print(f"Segunda nota registrada: {nota2}")
            break
    while True:
        nota3 = float(input("Ingrese la tercera nota del estudiante: "))
        if nota3 < 0 or nota3 > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
        else:
            print(f"Tercera nota registrada: {nota3}")
            break
    return nombre, edad, nota1, nota2, nota3


def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


def evaluar_desempeno(promedio):
    if promedio >= 4.5:
        return "Aprobado"
    elif promedio >= 3.5:
        return "En proceso de mejora"
    elif promedio >= 2.5:
        return "Regular"
    else:
        return "Deficiente"


prom = 0
contador = 0
while True:
    print("\n***Sistema de Gestión de Estudiantes***")
    print("1. Registrar estudiante")
    print("2. Salir")
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
        nombre, edad, nota1, nota2, nota3 = registro_estudiante()
        promedio = calcular_promedio(nota1, nota2, nota3)
        resultado = evaluar_desempeno(promedio)
        print(f"El promedio del estudiante {nombre} es: {promedio:.2f}")
        print(f"Desempeño: {resultado}")
        prom += promedio
        contador += 1
    elif opcion == "2":
        if contador > 0:
            print(
                f"El promedio general de los estudiantes registrados es: "
                f"{prom/contador:.2f}"
            )
            print(f"Total de estudiantes registrados: {contador}")
        else:
            print("No hay estudiantes registrados.")
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
