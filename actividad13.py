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
                estudiantes[id] = {"Nombre:" : nombre,
                                       "ID:" : id,
                                       "Carrera:" : carrera,
                                       "Cursos:" : {}}

        case 2:
            def agregar_cursos(curso, nota):
                solicitud_id = int(input("Ingresa el ID del estudiante: "))
                if solicitud_id in estudiantes:
                    curso = str(input("Ingresa el nombre del curso: "))
                    nota = int(input("Ingresa la nota final del estudiante: "))
                    if nota >= 0 and nota <= 100:
                        estudiantes[solicitud_id]["Cursos"][curso] = {"Curso: " : curso,
                                         "Nota:" : nota}
                    else:
                        print("La nota debe de estar en el rango de 0 - 100")
        def




