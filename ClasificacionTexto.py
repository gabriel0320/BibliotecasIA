import nltk
import random


# 1. Importación de bibliotecas:
# nltk: La biblioteca Natural Language Toolkit, que proporciona
# herramientas para procesamiento de lenguaje natural.
# random: Utilizado aquí para generar muestras aleatorias.
# Ejemplo de Clasificacion de Texto
# 2. Definición del conjunto de datos etiquetados
data =  [
    ("LOS LIMONES", "AMARILLO"),
    ("LOS PLÁTANOS", "AMARILLO"),
    ("LOS GIRASOLES", "AMARILLO"),
    ("EL SOL", "AMARILLO"),
    ("EL TAXI", "AMARILLO"),
    ("LAPIZ", "AMARILLO"),
    ("MOSTAZA", "AMARILLO"),
    ("EL CIELO", "AZUL"),
    ("EL OCÉANO", "AZUL"),
    ("JEANS", "AZUL"),
    ("ZAFIROS", "AZUL"),
    ("TURQUESAS", "AZUL"),
    ("AGUAMARINAS", "AZUL"),
    ("PÁJAROS AZULES", "AZUL"),
    ("LAS MANZANAS", "ROJO"),
    ("LAS ROSAS", "ROJO"),
    ("FRESAS", "ROJO"),
    ("CEREZAS", "ROJO"),
    ("MARTE", "ROJO"),
    ("BOMBEROS", "ROJO"),
    ("CORAZONES", "ROJO"),
    ("LOS RUBIES", "ROJO"),
    ("LAS NARANJAS", "AMARILLO"),
    ("LOS TOMATES", "ROJO"),
    ("EL FUEGO", "ROJO"),
    ("LAS BALLENAS", "AZUL"),
    ("LAS LUCES", "AZUL")
]


# 3. Preprocesamiento de datos:
# Preprocesar los datos Tockenizar y extraer  caracteristicas
# preprocess(text): Una función que toma un texto como entrada y realiza
# el preprocesamiento básico, que en este caso es la tokenización. Cada
# token (palabra) en el texto se convierte en una característica con un
# valor booleano verdadero (True).
def preprocesar(text):
    tokens = nltk.word_tokenize(text)
    return {word: True for word in tokens}

# 4. Aplicación del preprocesamiento a los datos:
# aplicacmos el procesamiento de datos
# featuresets: Una lista de tuplas donde cada tupla contiene un
# diccionario de características preprocesadas y su correspondiente
# etiqueta. Las características se extraen utilizando la función
# preprocess() y se almacenan como diccionarios.

featuresets = [(preprocesar(text), category) for (text, category) in data]

#  5. División de datos:
#  train_set, test_set: Se dividen los datos preprocesados en conjuntos de
# entrenamiento y prueba. Aquí, los primeros 16 elementos se utilizan
# para el conjunto de entrenamiento y el resto para el conjunto de prueba.

# Dividir datos en conjunto de entrenamiento y prueba (80% entrenamiento, 20% prueba) 

train_set, test_set = featuresets[:27], featuresets[:27]

# 6. Entrenamiento del clasificador:
# nltk.NaiveBayesClassifier.train(train_set): Se entrena un clasificador
# Naive Bayes utilizando el conjunto de entrenamiento.
classifier = nltk.NaiveBayesClassifier.train(train_set)

# 7. Prueba del clasificador:
# nltk.classify.accuracy(classifier, test_set): Se evalúa la precisión del
# clasificador en el conjunto de prueba y se imprime el resultado.

accuracy = nltk.classify.accuracy(classifier, test_set)


# 8. Clasificación de un texto:
# classifier.classify(preprocesar("el sol")): Se clasifica el texto utilizando
# el clasificador. El resultado se imprime en la consola.
#print("Clasificación de un texto: EL color del oceano es: ")

while True:
    print("Introduzca un objeto o Cosa para que obtenga su color: ")
    palabra =input()
    print( palabra, "es: ")
    print(classifier.classify(preprocesar(palabra.upper())))
    print("Precisión del clasificador:", accuracy)
    print("---------------------------------------")
    if palabra == "salir":
        break