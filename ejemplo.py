import joblib
import obtener_caracteristicas
import pandas as pd
import numpy as np

# Cargar el modelo
modelo = joblib.load("nombre_del_modelo.joblib")

# Cargamos el archivo sobre el que realizar las predicciones
df = pd.read_csv("archivo_a_predecir.csv")

# Dataframe en el que mostrar los resultados
resultados = pd.DataFrame()
resultados['CONTENIDO A ANALIZAR'] = df['comentario']

# Procesamos el dataframe
df = obtener_caracteristicas.main(df)

# Realizar la predicción
prediccion = modelo.predict(df)

# Si estamos utilizando el modelo MLP descomentamos lo siguiente:
# prediccion = np.argmax(prediccion, axis=1)
# prediccion += 1
# prediccion = np.ravel(prediccion)

# Añadimos las predcciones para visualizar los resultados
resultados['PREDICCIONES'] = prediccion
print(resultados)