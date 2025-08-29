# Modelo de clasificación de intensidades de discurso de odio

Este código implementa un sistema de clasificación de discurso de odio utilizando el modelo RoBERTuito (una versión en español de RoBERTa) para detectar intensidades de discurso de odio en tuits.

## Arquitectura del Modelo

El modelo se basa en `pysentimiento/robertuito-base-uncased` con las siguientes modificaciones:
- Se añadió una capa de clasificación densa con 4 salidas sobre el modelo base.
- Utiliza IDs de entrada y máscaras de atención como entradas.
- Genera una clasificación multiclase con 4 categorías (Incívicos, Malintencionado, Insulto, Amenaza).

## Datasets

1.  **Conjunto de Datos de Intensidades**: Este modelo utiliza un conjunto de datos personalizado para la clasificación de intensidades de discurso de odio, cargado desde `df_intensidades.csv`.
    -   Clasificación multiclase con las siguientes etiquetas:
        -   `0` = Intensidad 1 : Odio asociado a mensajes incívico
        -   `1` = MIntensidad 2 : Odio asociado a mensajes mal intencionados o con expresiones abusivas
        -   `2` = Intensidad 3 : Odio asociado a insultos
        -   `3` = Intensidad 4 : Odio asociado a amenazas veladas o explícitas

## Proceso de Entrenamiento

### Pre-entrenamiento
- Batch size: 16
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2

### Fine-tuning
- Batch size: 128
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2
- Métricas personalizadas (a definir según la tarea de clasificación multiclase).

## Métricas de Evaluación

El modelo se evalúa utilizando:
- Macro recall, precision, and F1-score
- One-vs-Rest AUC
- Accuracy
- Métricas por clase
- Matriz de confusión

## Requerimientos

Se requiere los siguientes paquetes de Python (consulte requirements.txt para ver la lista completa):
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn

## Uso
El modelo espera datos de entrada con las siguientes especificaciones:

1.  **Formato de datos**:
    -   Archivo CSV o DataFrame de Pandas
    -   Nombre de columna obligatorio: `text` (tipo cadena)
    -   Nombre de columna opcional: `label` (tipo entero, 0, 1, 2 o 3) si está disponible para la evaluación

2.  **Preprocesamiento de texto**:
    -   El texto se convertirá automáticamente a minúsculas durante el procesamiento
    -   Longitud máxima: 128 tokens (los textos más largos se truncarán)
    -   Los caracteres especiales, las URL y los emojis deben permanecer en el texto (el tokenizador los gestiona)

3.  **Codificación de etiquetas**:
    -   `0` = Intensidad 1 : Odio asociado a mensajes incívico
    -   `1` = Intensidad 2 : Odio asociado a mensajes mal intencionados o con expresiones abusivas
    -   `2` = Intensidad 3 : Odio asociado a insultos
    -   `3` = Intensidad 4 : Odio asociado a amenazas veladas o explícitas

El proceso de creación de este algoritmo se expone en el informe técnico localizado en: Blanco-Valencia, X., De Gregorio-Vicente, O., Ruiz Iniesta, A., & Said-Hung, E. (2025). Algoritmos de detección de odio/no odio, tipo e intensidad – Hatemedia V.2.0 (Version 2). Hatemedia Project. https://doi.org/10.5281/zenodo.16996080

Autores: 
- Xiomara Blanco
- Almudena Ruiz
- Daniel Pérez Palau
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz

Financiado por: 
MCIN/AEI /10.13039/501100011033

Como citar: Blanco Valencia, X., Pérez Palau, D., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. and Montero-Diaz, J. (2023), “Algorithm for classifying hate expressions by intensities in Spanish”, figshare. https://doi.org/10.6084/m9.figshare.25892815.

Más información:

- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net
- Este algoritmo está relacionado con el algoritmo de clasificación de odio/no odio, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- Este algoritmo está relacionado con el algoritmo de clasificación de expresiones de odio por tipo en español, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-type-in-Spanish

-------
# Hate Speech Intensity Classification Model

This code implements a hate speech classification system using the RoBERTuito model (a Spanish version of RoBERTa) to detect hate speech intensities in tweets.

##Model Architecture

The model is based on `pysentimiento/robertuito-base-uncased` with the following modifications:
- A dense classification layer with 4 outputs has been added over the base model.
- It uses input IDs and attention masks as inputs.
- It generates a multiclass classification with 4 categories (Uncivil, Malicious, Insult, Threat).

##Datasets

1. **Intensities Dataset**: This uses a custom dataset model for hate speech intensities classification, loaded from `df_intensidades.csv`.

- Multiclass classification with the following labels:
- `0` = Intensity 1: Hate associated with uncivil messages
- `1` = MIntensity 2: Hate associated with malicious messages or abusive language
- `2` = Intensity 3: Hate associated with insults
- `3` = Intensity 4: Hate associated with veiled or explicit threats

## Training Process

### Pre-training
- Batch size: 16
- Epochs: 5
- Learning rate: 2e-5 with 10% warm-up steps
- Stop early with patience = 2

### Fine Tuning
- Batch size: 128
- Epochs: 5
- Learning rate: 2e-5 with 10% warm-up steps
- Stop early with patience = 2
- Custom metrics (to be defined according to the training task) multiclass classification).

## Evaluation Metrics

The model is evaluated using:
- Macro recall, precision, and F1 score
- One-versus-rest AUC
- Accuracy
- Per-class metrics
- Confusion matrix

## Requirements

The following Python packages are required (see requirements.txt for the full list):
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn

## Usage
The model expects input data with the following specifications:

1. **Data Format**:
- CSV file or Pandas DataFrame
- Required column name: `text` (type string)
- Optional column name: `label` (type integer, 0, 1, 2, or 3) if available for evaluation

2. **Text Preprocessing**:
- Text is automatically converted to lowercase during processing
- Maximum length: 128 tokens (longer texts will be truncated)
- Special characters, URLs, and emojis must remain in the text (the tokenizer handles them)

3. **Label encoding**:
- `0` = Intensity 1: Hate associated with uncivil messages
- `1` = Intensity 2: Hate associated with malicious or abusive messages
- `2` = Intensity 3: Hate associated with insults
- `3` = Intensity 4: Hate associated with veiled or explicit threats

The process of creating this algorithm is explained in the technical report located at: Blanco-Valencia, X., De Gregorio-Vicente, O., Ruiz Iniesta, A., & Said-Hung, E. (2025). Algoritmos de detección de odio/no odio, tipo e intensidad – Hatemedia V.2.0 (Version 2). Hatemedia Project. https://doi.org/10.5281/zenodo.16996080

Authors:
- Xiomara Blanco
- Almudena Ruiz
- Daniel Pérez Palau
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz

Funded by:
MCIN/AEI/10.13039/501100011033

How to cites: Blanco Valencia, X., Pérez Palau, D., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. and Montero-Diaz, J. (2023), “Algorithm for classifying hate expressions by intensities in Spanish”, figshare. https://doi.org/10.6084/m9.figshare.25892815.

More information:

- https://www.hatemedia.es/ or contact: elias.said@unir.net
- This algorithm is related to the hate/non-hate classification algorithm, also developed by the authors: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- This algorithm is related to the algorithm for classifying hate expressions by types in Spanish, also developed by the authors: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-type-in-Spanish



