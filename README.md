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