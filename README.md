# Algorithm-for-classifying-hate-expressions-by-intensity-and-type-in-Spanish
Algoritmo de clasificación de expresiones de odio por intensidades en español. Este algoritmo fue desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/AEI /10.13039/501100011033, con la colaboración de Possible Inc.

Por favor lea el documento README IN SPANISH, en el que se expone todos los pasos a seguir para el uso del algoritmo desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/ AEI /10.13039/501100011033

El algoritmo permite la clasificación de expresiones de odio, de acuerdo a 4 tipos de intensidad de odio: 

- Intensidad 1 – Odio asociado a mensajes incívico
- Intensidad 2 – Odio asociado a mensajes mal intensionados o con expresiones abusivas
- Intensidad 3 – Odio asociado a insultos
- Intensidad 4 – Odio asociado a amenazas veladas o explícitas

La estructura de carpetas con la documentación de Github es la presentada a continuación:

        02 Documentación Github
         └── 01_Intensidades
             ├── DOCUMENTACIÓN GITHUB(1).docx
             ├── ejemplo.py
             ├── Modelo_intensidades.ipynb
             ├── obtener_caracteristicas.py
             └── recursos-20240304T124712Z-001.zip 

Se detalla a continuación el contenido de cada fichero:

- DOCUMENTACIÓN GITHUB.docx: Informe en el que se presenta el uso de los scripts ejemplo (1).py y obtener_caracteristicas (1).py para emplear los modelos.

- ejemplo (1).py: Script Python que muestra el uso de los modelos para realizar predicciones.

- Modelo_binario_(1) (1).ipnyb: Notebook con el código utilizado para el entrenamiento de los distintos modelos.

- Obtener_caracteristicas (1).py: Script Python con las funciones de preprocesado utilizadas previamente al uso de los modelos para predecir las entradas de un dataframe.

- Recursos-20231027T110710Z-001 (1).zip: La carpeta recursos contiene 3 .csv utilizados en la extracción de características.

El dataset que se ha utilizado para el entrenamiento de los modelos:
- Said-Hung, Elias; Montero-Diaz, julio; Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; et al. (2024). Dataset usado para entrenamientos de modelos de algoritmos de clasificación de odio, por tipos e intensidades (Dataset used to train hate classification algorithm models by types and intensities). figshare. Dataset. https://doi.org/10.6084/m9.figshare.26085700.v1

El Algoritmo fue desarrollado a partir de las pruebas de los modelos aplicados que se muestran en la carpeta MODELOS (https://acortar.link/e6hZSe). En esta carpeta se encuentran todos los resultados de los modelos utilizados durante el proceso de desarrollo de este algoritmo, con los respectivos porcentajes de entrenamiento y prueba.

El procedimiento seguido para entrenar los modelos queda reflejado en el Informe técnico Desarrollo del algoritmo de clasificación del odio por intensidades en medios digitales españoles en X (Twitter), Facebook y portales web:
- Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; José Cubillas, Juan; Said-Hung, Elias; et al. (2024). Informe técnico desarrollo de algoritmo de clasificación de odio por intensidades en medios informativos digitales españoles en X (Twitter), Facebook y portales web. figshare. Presentation. https://doi.org/10.6084/m9.figshare.25884262.v1

Autores: 
- Xiomara Blanco
- Almudena Ruiz
- Daniel Pérez Palau
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz
  
Financiado por: 
Agencia Estatal de Investigación – Ministerio de Ciencia e Innovación

Con el apoyo de:
- POSSIBLE S.L.

Como citar: Blanco Valencia, X., Pérez Palau, D., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. y Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por intensidades en español [Algorithm for classifying hate expressions by intensities in Spanish. https://doi.org/10.6084/m9.figshare.25892815.v1.

Más información:
- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net
- Este algoritmo está relacionado con el algoritmo de clasificación de odio/no odio, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
---
Algorithm for classifying hate expressions by intensities in Spanish. This algorithm was developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/AEI/10.13039/501100011033, with the collaboration of Possible Inc.

Please read README IN SPANISH, which outlines all the steps to follow to use the algorithm developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/AEI/10.13039/501100011033

The algorithm allows the classification of hate expressions according to 4 types of hate intensity: 

- Intensity 1 – Hate associated with uncivil messages
- Intensity 2 – Hatred associated with abusive expressions
- Intensity 3 – Hatred associated with insults
- Intensity 4 – Hatred associated with veiled or explicit threats

The folder structure with the GitHub documentation is presented below:

        02 Documentación Github
         └── 01_Intensidades
             ├── DOCUMENTACIÓN GITHUB(1).docx
             ├── ejemplo.py
             ├── Modelo_intensidades.ipynb
             ├── obtener_caracteristicas.py
             └── recursos-20240304T124712Z-001.zip

The content of each file is detailed below:

- DOCUMENTACIÓN GITHUB.docx:
Report that presents the example of the script (1).py and get_characteristics (1).py to use the models.

- ejemplo (1).py:
Python script showing the use of models to make predictions.

- Modelo_binario_(1) (1).ipnyb:
Notebook with the code used for training the different models.

- Obtener_caracteristicas (1).py:
Python script with the preprocessing functions used before using the models to predict the inputs of a data frame.

- Recursos-20231027T110710Z-001 (1).zip:
The resources folder contains 3 .csv used in feature extraction.

The dataset that has been used to build this library:
- Said-Hung, Elias; Montero-Diaz, julio; Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; et al. (2024). Dataset usado para entrenamientos de modelos de algoritmos de clasificación de odio, por tipos e intensidades (Dataset used to train hate classification algorithm models by types and intensities). figshare. Dataset. https://doi.org/10.6084/m9.figshare.26085700.v1

Results and comparisons generated during the training and validation process of the final model used for the development of the algorithm are shared in the document Comparativa_V2.xlsx; y Explicación variación resultados Odio_No odio V2.pdf (Por publicar)

The Algorithm was developed from the tests of the applied models shown in the MODELOS folder (https://acortar.link/e6hZSe). This folder contains all the results of the models used during the algorithm's development process, with the respective training and testing.

The procedure followed to train the models is reflected in the technical report Development of the hate classification algorithm by intensities in Spanish digital media in X (Twitter), Facebook and web portals:
- Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; José Cubillas, Juan; Said-Hung, Elias; et al. (2024). Informe técnico desarrollo de algoritmo de clasificación de odio por intensidades en medios informativos digitales españoles en X (Twitter), Facebook y portales web. figshare. Presentation. https://doi.org/10.6084/m9.figshare.25884262.v1

Authors:
- Xiomara Blanco
- Almudena Ruiz
- Daniel Pérez Palau
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz

Funded by:
State Research Agency – Ministry of Science and Innovation

With the support of:
- POSSIBLE S.L.

How to cites: Blanco Valencia, X., Pérez Palau, D., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. and Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por intensidades en español [Algorithm for classifying hate expressions by intensities in Spanish. https://doi.org/10.6084/m9.figshare.25892815.v1.

More information:
- https://www.hatemedia.es/ or contact: elias.said@unir.net
- This algorithm is related to the hate/non-hate classification algorithm, also developed by the authors: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
