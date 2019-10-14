# Detección de tríadas mediante redes neuronales

La idea es implementar [este paper](https://orbi.uliege.be/bitstream/2268/115963/1/Osmalskyj2012Neural.pdf)
donde siguen los siguentes pasos:

1. Armar CSVs para cada audio con el PCP que representa cada acorde
  (esta viene a ser la parte más difícil)
2. Entrenar una red neuronal con los PCPs anteriores
3. ...
4. Profit!

Este repo tiene tres scripts:
* `preparar_datos.py` que hace el primer punto y deja los archivos `train.csv` y `test.csv`
  que son los archivos para entrenar y para probar la red, respectivamente
* `entrenar.py` que usa `train.csv` para entrenar una red neuronal (armada con Keras y Tensorflow).
  Guarda el modelo que arma en el archivo `modelo.h5`
* `evaluar.py` que usa el modelo y lo prueba con un set de datos de prueba

## Para arrancar
1. Tener `virtualenv` instalado
2. `$ virtualenv .` (sólo la primer vez, para armar el ambiente)
3. `$ source bin/activate`
4. `$ pip install -r requirements.txt`
5. `$ deactivate` (cuando quieras salir del ambiente virtual)