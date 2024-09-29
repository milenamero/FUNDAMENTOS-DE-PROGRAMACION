# Función para calcular el promedio de temperatura de una ciudad durante un periodo de tiempo
def calcula_promedio_temperatura(temperaturas):
    total_semanas = len(temperaturas)
    total_dias = len(temperaturas[0])
    suma_total = 0

    for semana in temperaturas:
        for dia in semana:
            suma_total += dia["temp"]

    # Calculamos el promedio total
    promedio = suma_total / (total_semanas * total_dias)
    return promedio


# Ejemplo de uso con los datos de temperaturas de una ciudad (4 semanas)
temperaturas_portoviejo = [
    [  # Semana 1
        {"day": "Lunes", "temp": 31},
        {"day": "Martes", "temp": 32},
        {"day": "Miércoles", "temp": 32},
        {"day": "Jueves", "temp": 31},
        {"day": "Viernes", "temp": 30},
        {"day": "Sábado", "temp": 30},
        {"day": "Domingo", "temp": 30}
    ],
    [  # Semana 2
        {"day": "Lunes", "temp": 30},
        {"day": "Martes", "temp": 31},
        {"day": "Miércoles", "temp": 31},
        {"day": "Jueves", "temp": 32},
        {"day": "Viernes", "temp": 33},
        {"day": "Sábado", "temp": 31},
        {"day": "Domingo", "temp": 33}
    ],
    [  # Semana 3
        {"day": "Lunes", "temp": 29},
        {"day": "Martes", "temp": 30},
        {"day": "Miércoles", "temp": 28},
        {"day": "Jueves", "temp": 33},
        {"day": "Viernes", "temp": 27},
        {"day": "Sábado", "temp": 26},
        {"day": "Domingo", "temp": 30}
    ],
    [  # Semana 4
        {"day": "Lunes", "temp": 28},
        {"day": "Martes", "temp": 30},
        {"day": "Miércoles", "temp": 29},
        {"day": "Jueves", "temp": 30},
        {"day": "Viernes", "temp": 28},
        {"day": "Sábado", "temp": 28},
        {"day": "Domingo", "temp": 29}
    ]
]

# Llamada a la función y mostrar resultado
promedio_portoviejo = calcula_promedio_temperatura(temperaturas_portoviejo)
print(f"El promedio de temperatura en Portoviejo es: {promedio_portoviejo:.2f} grados")

