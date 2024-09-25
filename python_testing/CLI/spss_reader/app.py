import pyreadstat

# Path to your SPSS file
file_path = 'archivoleible.sav'

# Read the SPSS file
df, meta = pyreadstat.read_sav(file_path)

# Print the first few rows of the dataframe to understand its structure
print(df.head())

# If you're interested in specific variables (columns), you can select them like this
selected_variables = df[['variable1', 'variable2']]

# If you need to filter the data (e.g., select rows where some condition is met), you can do it like this
filtered_data = df[df['variable'] > some_value]

# To explore metadata (like variable labels), you can do:
print(meta.column_labels)

