# Actividad 5 - MLOps con MLflow

proyecto de clasificación binaria usando el dataset Breast Cancer Wisconsin.

## Modelos entrenados
- Logistic Regression
- Random Forest

## Métricas
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Herramientas
- Google Colab
- scikit-learn
- MLflow
- pandas
- matplotlib
- seaborn

## Ejecución
1. Ejecutar el notebook `fuentes/entrena.ipynb`.
2. Generar datasets en `datos/datos_ini` y `datos/datos_limp`.
3. Entrenar modelos con GridSearchCV.
4. Registrar métricas y artefactos en MLflow.
5. Revisar resultados en la carpeta `results`.

## Conclusión
El mejor modelo se selecciona comparando F1-score, ROC-AUC y estabilidad general.
