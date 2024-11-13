from fastapi import FastAPI,Query # Importamos la libreria FastAPI
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
#from fastapi.responses import HTMLResponse
from typing import Optional

import nltk # Importamos la libreria Optional para volver parametros opcionales

movies_list = [
    {
        "id": 1,
        "title": "Inception",
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "year": 2010,
        "rating": 8.8,
        "category": "action"
    },
    {
        "id": 2,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "year": 1994,
        "rating": 9.3,
        "category": "drama"
    },
    {
        "id": 3,
        "title": "The Godfather",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": 1972,
        "rating": 9.2,
        "category": "action"
    },
    {
        "id": 4,
        "title": "The Dark Knight",
        "overview": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        "year": 2008,
        "rating": 9.0,
        "category": "action"
    },
    {
        "id": 5,
        "title": "Pulp Fiction",
        "overview": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "year": 1994,
        "rating": 8.9,
        "category": "fiction"
    }
]


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

@app.get("/movies/tokenize")
def tokenize(text: str = Query(...)):
    processed_text = preprocesar(text)
    return {"processed_text": processed_text}

def preprocesar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return json.dumps(result)

# para correr la app: uvicorn main:app --reload
# uvicorn nombreApp:app --reload --port 5000 
# swagger: http://127.0.0.1:5000/docs#/