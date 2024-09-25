# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:16:58 2024

@author: Usuario Asignado
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Generar un conjunto de datos de ejemplo
X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=42)

# Escalar los datos para tener media 0 y varianza 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Inicializar PCA, elegir el número de componentes a conservar
pca = PCA(n_components=8)

# Ajustar PCA al conjunto de datos y transformarlo
X_pca = pca.fit_transform(X_scaled)


# Imprimir la varianza explicada por cada componente principal
print("Varianza explicada por cada componente: %s" % pca.explained_variance_ratio_)

# Imprimir la varianza total explicada
print("Varianza total explicada: %0.2f" % sum(pca.explained_variance_ratio_))

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=40)
plt.title("PCA - Primeros dos componentes principales")
plt.xlabel("Primer componente principal")
plt.ylabel("Segundo componente principal")
plt.colorbar(label='Clase')
plt.show()

# Reducir a 2 componentes para visualización
pca_2 = PCA(n_components=2)
X_pca_2 = pca_2.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(X_pca_2[:, 0], X_pca_2[:, 1], c=y, cmap='viridis', edgecolor='k', s=40)
plt.title("PCA a 2 Componentes Principales")
plt.xlabel("1er Componente Principal")
plt.ylabel("2do Componente Principal")
plt.colorbar(label='Clase')
plt.show()

