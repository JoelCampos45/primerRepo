class estudiante:

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 10

    def verificarEdad(self):
        print("la  edad del usuario es : ")
        print(str(self.edad))


est1 = estudiante()

est1.nombre = "Joel"
est1.apellido = "campos"
est1.edad = 18

print("Imprimiendo los datos del estudiante 1")
print(est1.nombre)
print(est1.apellido)
print(str(est1.edad))

est2 = estudiante()
est2.nombre = "diego"
est2.apellido = "diaz"
est2.edad = 25

print("Imprimiendo los datos del estudiante 2")
print(est2.nombre)
print(est2.apellido)
print(str(est2.edad))


print("impriendo los tipos de est1 y est2")
print(type(est1))
print(type(est2))

lista_estudiante = [est1, est2]

print("se imprimen los nombres de los estudiantes creados")
for alumno in lista_estudiante:
    print(alumno.nombre)

est1.verificarEdad()
est2.verificarEdad()
