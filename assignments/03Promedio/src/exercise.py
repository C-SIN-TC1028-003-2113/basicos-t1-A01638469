def main():
    #escribe tu código abajo de esta línea
    cal_suma = float(input('Calificación de la materia: '))
    cal_suma += float(input('Calificación de la materia: '))
    cal_suma += float(input('Calificación de la materia: '))
    cal_suma += float(input('Calificación de la materia: '))
    promedio_final = cal_suma / 4
    print('El promedio es: ' + str(promedio_final))


if __name__ == '__main__':
    main()
