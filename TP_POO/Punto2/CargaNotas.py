

class CargarNotas:
    def __init__(self):
        pass
    alumnos = []

    
    def main (self):
        salirAlumno = False
        salirNotas = False
        salir = "n"
        while(salirAlumno == False):
            alumno = Alumno()
            print("Ingrese los datos del alumno")
            alumno.nombreCompleto = input("Ingrese el nombre completo: ")
            alumno.legajo = input("Ingrese el legajo: ")
            
            while(salirNotas == False):
                notas = Nota()
                notas.catedra = input("Ingrese el nombre de la catedra: ")
                notas.notaExamen = input("Ingrese la nota")
                salir == input("Desea salir? (Y/N): ").lower
                if (salir == "y"):
                    salirNotas == True
                alumno.notas.append(notas.notaExamen)
                
                
            
CargarNotas.main


        

        
