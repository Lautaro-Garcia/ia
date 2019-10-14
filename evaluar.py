from tensorflow import keras
import numpy as np

from cargar_datos import cargar_datos

acordes_prueba, nombres_acordes_prueba = cargar_datos('evaluacion.csv')
model = keras.models.load_model('modelo.h5')
test_loss, test_acc = model.evaluate(acordes_prueba,  nombres_acordes_prueba, verbose=2)
predicciones = model.predict(acordes_prueba)
1+1