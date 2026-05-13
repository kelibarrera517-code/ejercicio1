print("PROGRAMA DE CALIFICACIONES")
print("Bienvenido")

while True:
    print("Escriba el nombre del estudiante:")
    nombre = input("Ingrese su nombre: ")
    suma = 0

    print("Escriba las 5 notas del estudiante:")
    for i in range(5):
        nota = input("Digite una nota: ")

        while nota == "a" or nota == "b" or nota == "c" or nota == "d" or nota == "e" or nota == "f" or nota == "g" or nota == "h" or nota == "i" or nota == "j" or nota == "A" or nota == "B" or nota == "C" or nota == "D" or nota == "E" or nota == "F" or nota == "G" or nota == "H" or nota == "I" or nota == "J":

            print("Error, la nota no puede ser una letra")
            nota = input("Escriba una nota: ")

        nota = float(nota)

        while nota > 5:
            print("Error, la nota no puede ser mayor que 5")
            nota = float(input("Escriba una nota: "))

        while nota < 0:
            print("Error, la nota no puede ser menor que 0")
            nota = float(input("Escriba una nota: "))

        suma = suma + nota

    promedio = suma / 5

    print("Estudiante:", nombre)
    print("Promedio:", promedio)

    if promedio == 5:
        print("Excelente")

    elif promedio >= 4:
        print("Aprobó")

    elif promedio >= 3:
        print("Reprobó")

    else:
        print("Reprobó")

    continuar = input("¿Desea ingresar otro estudiante? (si/no): ")

    if continuar == "no":
        break
