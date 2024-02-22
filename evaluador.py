def calcularpromedio(notas):
    promedio = sum(notas)/ len(notas)
    return promedio


def evaluar(promedio):
    if promedio >= 4:
        return "Aprobado"
    else:
        return "reprobado"

def main():
    ramos = ["lenguaje", "matematicas", "historia"]
    notas = []

    for ramo in ramos:
        while True:
            nota = float(input(f"ingrese la nota de {ramo}: "))
            if nota >= 1 or nota <= 7:
                notas.append(nota)
                break
            else:
                print("porfavor ingrese una nota entre el 1 y el 7")
    
    promedio =calcularpromedio(notas)
    resultado = evaluar(promedio)

    print(f"el promedio total es: {promedio}")
    print(f"el estudiante esta {resultado}")

if __name__ == "__main__":
    main()