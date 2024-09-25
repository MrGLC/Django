from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd

# Cargamos tus datos
file_path = 'Processed_Dataset.xlsx'
data = pd.read_excel(file_path)

# Imputación de NaNs (opción 2)
imputer = SimpleImputer(strategy='mean')  # Puedes ajustar la estrategia de imputación según sea necesario
data_imputed = imputer.fit_transform(data)

# Convertimos de nuevo a DataFrame si deseas mantener la estructura para futuras operaciones
data_imputed = pd.DataFrame(data_imputed, columns=data.columns)

# Aplicamos PCA para explorar la varianza explicada
pca_full = PCA()
pca_full.fit(data_imputed)

# Calculamos cuántos componentes son necesarios para explicar al menos el 95% de la varianza
varianza_explicada_cumulativa = pca_full.explained_variance_ratio_.cumsum()
n_components_95 = (varianza_explicada_cumulativa < 0.95).sum() + 1

# Aplicamos PCA con el número de componentes calculado
pca = PCA(n_components=n_components_95)
X_pca = pca.fit_transform(data_imputed)

# `X_pca` ahora contiene tus datos transformados en un espacio de menor dimensión
print(f"Número de componentes para explicar al menos el 95% de la varianza: {n_components_95}")


# Vectores propios: cómo cada característica contribuye a cada componente principal
print("Vectores propios (carga de las características):")
print(pca.components_)

# Varianza explicada por cada componente
print("Varianza explicada por cada componente:")
print(pca.explained_variance_ratio_)

# Para un resumen más detallado, podemos crear un DataFrame
import pandas as pd

components_df = pd.DataFrame(pca.components_, columns=data.columns, index=[f'PC{i+1}' for i in range(n_components_95)])
print(components_df)

