import pandas as pd

# Load the dataset from an Excel file
df = pd.read_excel('Processed_Dataset.xlsx')

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Save the correlation matrix to a new Excel file
correlation_matrix.to_excel('correlation_matrix.xlsx')

print(correlation_matrix)

