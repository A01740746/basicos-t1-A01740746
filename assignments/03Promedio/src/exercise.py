def main():
    #escribe tu código abajo de esta línea
    Materia1 = float(input("Calificación de la materia: "))
    Materia2 = float(input("Calificación de la materia: "))
    Materia3 = float(input("Calificación de la materia: "))
    Materia4 = float(input("Calificación de la materia: "))
    
    Promedio = (Materia1 + Materia2 + Materia3 + Materia4)/4

    print("El promedio es: " + str(Promedio))

if __name__ == '__main__':
    main()
