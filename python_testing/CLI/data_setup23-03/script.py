import pandas as pd
import numpy as np

# Read the modified Excel file
df = pd.read_excel('example.xlsx')

# Create a correlation matrix
corr_matrix = df.corr()

# Save the correlation matrix to a new Excel file
corr_matrix.to_excel('correlation_matrix.xlsx', index=True, header=True)
