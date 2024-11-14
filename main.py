from fastapi import FastAPI,Query # Importamos la libreria FastAPI
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
from fastapi.responses import HTMLResponse
from typing import Optional

import nltk # Importamos la libreria Optional para volver parametros opcionales
import json


def leer_peliculas_desde_json(archivo_json):
    with open(archivo_json, 'r', encoding='utf-8') as file:
        peliculas = json.load(file)
    return peliculas

# Uso de la función
archivo_json = 'movies.json'
movies_list = leer_peliculas_desde_json(archivo_json)



def guardar_peliculas_en_json(lista_peliculas, archivo_json):
    with open(archivo_json, 'w', encoding='utf-8') as file:
        json.dump(lista_peliculas, file, ensure_ascii=False, indent=4)

# Uso de las funciones
archivo_json = 'movies.json'



app = FastAPI() # Creamos una instancia de la libreria FastAPI
#para el Swagger:
app.title = "Mi primer API con FastAPI Framework" # Asignamos un titulo a la API
app.version = "0.0.1" # Asignamos una version a la API
@app.get("/",tags=["home"]) # Decorador para indicar que es una ruta de la API
def message(): # Funcion que retorna un mensaje
    #return HTMLResponse('<h1>¡Bienvenido a mi API!</h1>')
    return JSONResponse(content={"message": "¡Bienvenido a mi API!"})

@app.get("/movies",tags=["Movies"]) # Decorador para indicar que es una ruta de la API
def movies(): # Funcion que retorna un mensaje
    return movies_list
#uso de parametros
@app.get("/movies/{id}") # Decorador para indicar que es una ruta de la API
def get_movies(id:int): # Funcion que retorna un mensaje
    for item in movies_list:
        if item["id"] == id:
            return  item
     
    return JSONResponse(content={"message": "Pelicula no encontrada"})
    
# Flitrado de peliculas por categorias
@app.get("/movies/",tags=["Movies"]) 
def get_movies_by_category(category:Optional[str],year:Optional[int]): # Decorador para indicar que es una ruta de la API
    return [movie for movie in movies_list if movie["category"] == category or movie["year"] == year]

#POST para adicionar pelicula dado un json
@app.post("/movies/",tags=["Movies"]) # Decorador para indicar que es una ruta de la API
def add_movie(movie:dict): # Funcion que retorna un mensaje
    movies_list.append(movie)
    guardar_peliculas_en_json(movies_list, archivo_json)
    return JSONResponse(content={"message": "Pelicula agregada"})
#PUT para actualizar pelicula dado un json
@app.put("/movies/",tags=["Movies"]) # Decorador para indicar que es una ruta de la API
def update_movie(id:int,movie:dict): # Funcion que retorna un mensaje
    for item in movies_list:
        if item["id"] == id:
            item.update(movie)
            return JSONResponse(content={"message": "Pelicula actualizada"})
    return JSONResponse(content={"message": "Pelicula no encontrada"})
#DELETE para eliminar pelicula dado un json
@app.delete("/movies/",tags=["Movies"]) # Decorador para indicar que es una ruta de la API
def delete_movie(id:int): # Funcion que retorna un mensaje
    for item in movies_list:
        if item["id"] == id:
            movies_list.remove(item)
            return JSONResponse(content={"message": "Pelicula eliminada"})
    return JSONResponse(content={"message": "Pelicula no encontrada"})

#Tokenizar
@app.post("/tokenize") # Decorador para indicar que es una ruta de la API
def tokenize(text:str): # Funcion que retorna un mensaje
    return preprocessar(text)


def preprocessar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return JSONResponse(content={"message":result})

# para correr la app: uvicorn main:app --reload
# uvicorn nombreApp:app --reload --port 5000 
# swagger: http://127.0.0.1:5000/docs#/