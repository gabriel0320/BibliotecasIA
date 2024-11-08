import nltk
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

# NNP - Proper Noun, Singular (Nombre propio, singular): NLTK
# CC - Coordinating Conjunction (Conjunción coordinante): es
# JJ - Adjective (Adjetivo): una, natural
# NN - Noun, Singular (Sustantivo, singular): biblioteca
# IN - Preposition or Subordinating Conjunction (Preposición o conjunción subordinante): de
# FW - Foreign Word (Palabra extranjera): procesamiento, lenguaje

nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk import word_tokenize

text = "NLTK es una biblioteca de python para procesamiento de lenguaje natural."
tokens = word_tokenize(text)
tagged_words = pos_tag(tokens)
print("Ejemplo 3 de Etiquetado: ")
print(tagged_words)