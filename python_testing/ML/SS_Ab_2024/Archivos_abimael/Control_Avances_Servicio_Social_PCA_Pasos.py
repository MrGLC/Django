# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:55:40 2024

@author: Usuario Asignado
"""


import numpy as np
import matplotlib.pyplot as plt


# Generar datos simulados
# np.random.seed(0)  # Para reproducibilidad
# X = np.dot(np.random.rand(2, 2), np.random.randn(2, 200)).T

X=np.array([[126,  78],
       [128,  80],
       [128,  82],
       [130,  82],
       [130,  84],
       [132,  86]])

# centrar los datos
X = (X - np.mean(X, axis=0))


# Visualizar los datos originales
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1])
plt.title("Datos Originales")
plt.xlabel("X1")
plt.ylabel("X2")
plt.axis('equal')
plt.show()

# Calcular la matriz de covarianza
CovMatrix = np.cov(X.T)
CoRMatrix = np.corrcoef(X.T)
print("Matriz de Covarianza:\n", CovMatrix)
print("Matriz de Correlación:\n", CoRMatrix)

#calcular eigenvalores y eigenvectores
eigenvalues, eigenvectors = np.linalg.eig(CovMatrix)

print("Eigenvalores:\n", eigenvalues)
print("Eigenvectores:\n", eigenvectors)


######################################################
# Graficar los datos junto con los eigenvectores
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
for i in range(len(eigenvalues)):
    plt.arrow(0, 0, eigenvectors[0, i] * eigenvalues[i],
              eigenvectors[1, i] * eigenvalues[i], 
              head_width=0.05, head_length=0.1, 
              linewidth=2, color='red', alpha=0.5)
plt.title("Eigenvectores")
plt.xlabel("X1")
plt.ylabel("X2")
plt.axis('equal')
plt.show()
#######################################################
# Ordenar los eigenvalores y eigenvectores
idx = eigenvalues.argsort()[::-1]   
eigenvalues_sorted = eigenvalues[idx]
eigenvectors_sorted = eigenvectors[:,idx]

#####################################################3
# Generar la matriz de proyección
projection_matrix = eigenvectors_sorted

print("Matriz de Proyección:\n", projection_matrix)


#############################################################
# Proyectar los datos
X_pca = X.dot(projection_matrix)

# Visualizar los datos proyectados
plt.figure(figsize=(6, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title("Datos Proyectados")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.axis('equal')
plt.show()

########################################################
#calcular la variabilidad explicada de los componentes

# Ordenar los eigenvalores de mayor a menor
eigenvalues_sorted = sorted(eigenvalues, reverse=True)

# Calcular la suma total de los eigenvalores
Suma_eigenvalores= sum(eigenvalues)

# Inicializar una lista para guardar el porcentaje de varianza explicada
variance_explained = []

# Calcular el porcentaje de varianza explicada por cada eigenvalor
for eigenval in eigenvalues_sorted:
    percentage = (eigenval / Suma_eigenvalores) * 100
    variance_explained.append(percentage)

print("Porcentaje de Varianza Explicada por cada componente:", variance_explained)
##########################################################

# Eliminar el componente con menor varianza

# Identificar el índice del componente principal con la mayor varianza explicada
index_max_variance = np.argmax(variance_explained)

# Mantener solo el componente principal con mayor varianza explicada
X_pca_reduced = X_pca[:, index_max_variance]

# Visualizar los datos proyectados solo con ese componente principal
plt.figure(figsize=(6, 4))
plt.scatter(X_pca_reduced, np.zeros_like(X_pca_reduced), alpha=0.7)
plt.title(f"Datos en el Componente Principal con Mayor Varianza Explicada (PC{index_max_variance+1})")
plt.xlabel(f"Componente Principal {index_max_variance+1}")
plt.yticks([])  # Eliminar marcas del eje y ya que no aportan información en este contexto
plt.show()


#########################################################
#########################################################
#opcional

import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

X=np.array([[126,  78],
       [128,  80],
       [128,  82],
       [130,  82],
       [130,  84],
       [132,  86]])

# Escalar los datos para tener una mejor visualización
X = (X - np.mean(X, axis=0))

# Inicializar PCA, elegir el número de componentes a conservar
pca = PCA(n_components=1)

# Ajustar PCA al conjunto de datos y transformarlo
X_pca = pca.fit_transform(X)


# Imprimir la varianza explicada por cada componente principal
print("Varianza explicada por cada componente: %s" % pca.explained_variance_ratio_)

# Imprimir la varianza total explicada
print("Varianza total explicada: %0.2f" % sum(pca.explained_variance_ratio_))

plt.figure(figsize=(8, 6))
plt.scatter(X_pca, np.zeros_like(X_pca), alpha=0.7)
# plt.scatter(X_pca[:, 0], X_pca[:, 1], cmap='viridis', edgecolor='k', s=40)
plt.title("PCA - Primer componente principales")
plt.xlabel("Primer componente principal")
plt.ylabel("Segundo componente principal")
plt.show()
