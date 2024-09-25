import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset procesado
df = pd.read_excel('Processed_Dataset.xlsx')

# Seleccionar solo las columnas numéricas para la matriz de correlación
numeric_df = df.select_dtypes(include=[np.number])

# Calcular la matriz de correlación de Pearson
corr_matrix = numeric_df.corr()

# Visualizar la matriz de correlación
plt.figure(figsize=(10, 10))
plt.matshow(corr_matrix, fignum=1)
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

# Mostrar la barra de colores
plt.colorbar()
plt.title('Matriz de Coeficientes de Correlación', y=1.15)
plt.tight_layout()
plt.show()

