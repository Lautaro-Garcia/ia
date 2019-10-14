import csv
import glob
import soundfile as sf
import numpy as np

NOTAS = ['a', 'am', 'bm', 'c', 'd', 'dm', 'e', 'em', 'f', 'g']

frecuencias_de_referencia = [
    130.80,
    138.59,
    146.83,
    155.56,
    164.81,
    174.61,
    185.00,
    196.00,
    207.65,
    220.00,
    233.08,
    246.94,
]


def delta(x, y):
    return 1 if x == y else 0


def procesar_audio(path_del_audio):
    muestras, frecuencia_muestreo = sf.read(path_del_audio)
    transformadas = np.fft.rfft(muestras[:16386])
    cantidad_bins = len(transformadas)

    def pcp(clase_de_nota):
        def m(indice):
            if indice is 0:
                return -1
            return np.mod(np.round(12 * np.log2(
                frecuencia_muestreo * indice / (cantidad_bins * frecuencias_de_referencia[clase_de_nota]))), 12)

        def pcp_interno(indice):
            return (np.linalg.norm(transformadas[indice]) ** 2) * delta(m(indice), clase_de_nota)

        return np.sum(list(map(pcp_interno, range(0, cantidad_bins))))

    pcp_array = np.array(list(map(pcp, range(0, 12))))
    return pcp_array / np.sum(pcp_array)


def nota_posta(filename):
    return NOTAS.index(''.join(filter(lambda x: not x.isdigit(), filename.split('.')[0])))


def guardar_pcp(path_samples, nombre_archivo_salida):
    float_formatter = lambda x: "%.5f" % x

    np.set_printoptions(formatter={'float_kind': float_formatter})

    with open(nombre_archivo_salida, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for filepath in glob.iglob(path_samples + '/**/*.wav', recursive=True):
            vector_pcp = np.append(procesar_audio(filepath), int(nota_posta(filepath.split('/')[-1])))
            print("Escribiendo ", vector_pcp)
            writer.writerow(vector_pcp)

procesar_audio('train_samples/Guitar_Only/a/a61.wav')
# guardar_pcp('train_samples', 'notas.csv')
# guardar_pcp('test_samples', 'evaluacion.csv')