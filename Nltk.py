import nltk
import random
#  DEscargar el paquete NLTK 
# nltk.download()


#EJEMPLO DE TOKENIZACION 
#División de una oración en palabras individuales. Usando NLTK, se puede
#tokenizar una oración en palabras individuales, lo que facilita el análisis
#posterior del texto.
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "NLTK es una biblioteca de python para procesamiento de lenguaje natural."

tokens = word_tokenize(text)
print("Ejemplo 1 de tokenizacion: ")
print(tokens)


# Ejemplo de Derivacion
#Reducción de palabras a su forma base. Con NLTK, se puede realizar la
#derivación de palabras para reducirlas a su forma base.

from nltk.stem import PorterStemmer

words = ["program", "programs", "programer", "programing", "programers"]
stemmer = PorterStemmer()
steam_words = [stemmer.stem(w) for w in words]
print("Ejemplo 2 de Derivacion de palabras: program, programs, programer, programing, programers: ")
print(steam_words)

# Ejemplo de Etiquetado
#El etiquetado en NLTK implica asignar etiquetas a las palabras en un texto
#para indicar su función gramatical o su categoría semántica. Por ejemplo, en
#el etiquetado gramatical, cada palabra puede ser etiquetada como sustantivo,
#verbo, adjetivo, etc. En el etiquetado semántico, las palabras pueden ser
#etiquetadas según su sentido o significado en el contexto específico. NLTK
#proporciona herramientas para realizar tanto el etiquetado gramatical como
#el semántico utilizando algoritmos de aprendizaje automático o reglas
#ingüísticas.

nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk import word_tokenize

text = "NLTK es una biblioteca de python para procesamiento de lenguaje natural."
tokens = word_tokenize(text)
tagged_words = pos_tag(tokens)
print("Ejemplo 3 de Etiquetado: ")
print(tagged_words)

# 1. Importación de bibliotecas:
# nltk: La biblioteca Natural Language Toolkit, que proporciona
# herramientas para procesamiento de lenguaje natural.
# random: Utilizado aquí para generar muestras aleatorias.
# Ejemplo de Clasificacion de Texto
# 2. Definición del conjunto de datos etiquetados
data = [
    ("los Limones ", "amarillo"),
    ("Limones ", "amarillo"),
    ("los Plátanos ", "amarillo"),
    ("los Girasoles ", "amarillo"),
    ("El sol ", "amarillo"),
    ("El Taxi ", "amarillo"),
    ("Lapiz ", "amarillo"),
    ("Motaza ", "amarillo"),
    ("El cielo", "azul"),
    ("El océano", "azul"),
    ("Jeans", "azul"),
    ("Zafiros", "azul"),
    ("Turquesas", "azul"),
    ("Aguamarinas", "azul"),
    ("Pájaros azules", "azul"),
    ("Las Manzanas", "rojo"),
    ("las Rosas", "rojo"),
    ("Fresas", "rojo"),
    ("Cerezas", "rojo"),
    ("Marte", "rojo"),
    ("Bomberos", "rojo"),
    ("Corazones", "rojo")
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

train_set, test_set = featuresets[:16], featuresets[16:]

# 6. Entrenamiento del clasificador:
# nltk.NaiveBayesClassifier.train(train_set): Se entrena un clasificador
# Naive Bayes utilizando el conjunto de entrenamiento.
classifier = nltk.NaiveBayesClassifier.train(train_set)

# 7. Prueba del clasificador:
# nltk.classify.accuracy(classifier, test_set): Se evalúa la precisión del
# clasificador en el conjunto de prueba y se imprime el resultado.

accuracy = nltk.classify.accuracy(classifier, test_set)
print("Precisión del clasificador:", accuracy)

# 8. Clasificación de un texto:
# classifier.classify(preprocesar("el sol")): Se clasifica el texto utilizando
# el clasificador. El resultado se imprime en la consola.
print("Clasificación de un texto: EL color del Marte es: ")
print(classifier.classify(preprocesar("Marte")))