import csv
import numpy as np


def cargar_datos(nombre_archivo):
    datos_entrenamiento = []
    nombres_entrenamiento = []
    with open(nombre_archivo, newline='') as csvfile:
        for fila in csv.reader(csvfile):
            datos_entrenamiento.append(list(map(lambda x: float(x), fila[:-1])))
            nombres_entrenamiento.append(float(fila[-1]))

    return np.array(datos_entrenamiento), np.array(nombres_entrenamiento)