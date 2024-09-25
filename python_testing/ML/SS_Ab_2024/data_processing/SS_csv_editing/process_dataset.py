import pandas as pd

# Cargar el dataset
df = pd.read_excel('database.xlsx')

# Normalizar las columnas tipo "1"
columns_to_normalize = [col for col in df.columns if col.startswith('1')]
for col in columns_to_normalize:
    min_val = df[col].min()
    max_val = df[col].max()
    df[col] = (df[col] - min_val) / (max_val - min_val)

# Eliminar las columnas tipo "2"
columns_to_drop = [col for col in df.columns if col.startswith('2')]
df.drop(columns=columns_to_drop, inplace=True)

# Normalizar las columnas tipo "3"
columns_to_normalize_type_3 = [col for col in df.columns if col.startswith('3')]
for col in columns_to_normalize_type_3:
    unique_values = df[col].unique()
    if set(unique_values).issubset({-1, 1}):
        df[col] = (df[col] + 1) / 2
    else:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)

# Las columnas tipo "4" se mantienen sin cambios ya que son los targets

# Guarda el dataframe modificado en un nuevo archivo Excel
df.to_excel('Processed_Dataset.xlsx', index=False)

