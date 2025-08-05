estudiantes = {}

while True:
    print("\nBienvenido al menú")
    print("1. Agregar estudiante")
    print("2. Agregar curso con nota")
    print("3. COnsultar estudiante")
    print("4. Calcular promedio de estudiante")
    print("5. Verificar si el estudiante aprueba")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir")

    option = int(input("Ingresa una opción del menú (1-7): "))
    match option:
        case 1:
            def agregar_estudainte(id, nombre, carrera):
                id = int(input("Ingrese el id del estudiante: "))
                nombre = str(input("Ingresa el nombre del estudiante: "))
                carrera = str(input("Ingresa la carrera o programa académico del estudiante: "))
                estudiantes[nombre] = {"Nombre:" : nombre,
                                       "ID:" : id,
                                       "Carrera:" : carrera}
                for id in estudiantes:
                    cursos = {}

            def agregar_cursos(curso, nota):
