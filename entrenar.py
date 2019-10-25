#!bin/python3.7
from tensorflow import keras

from cargar_datos import cargar_datos

acordes_entrenamiento, nombres_acordes_entrenamiento = cargar_datos('train.csv')

model = keras.Sequential([
    keras.layers.Dense(12, input_shape=(12,)),
    keras.layers.Dense(35, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='sgd',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(acordes_entrenamiento, nombres_acordes_entrenamiento, epochs=2000)

model.save('modelo.h5')