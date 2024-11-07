import sklearn

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Cargarel conjunto de datos California Housing
California_Housing = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(California_Housing.data, California_Housing.target, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model= LinearRegression()
# Entrenar el modelo
model.fit(X_train, y_train)
# Predecir las etiquetas para los dtos de prueba
y_pred = model.predict(X_test)
# Calcular error cuadratico medio
mse = mean_squared_error(y_test, y_pred)

print('Error cuadratico medio:', mse)