import pandas as pd
import os

# Set directory folders to store our data
dirname = os.getcwd()

raw_data = f"{dirname}/data/raw/"
transformed_data = f"{dirname}/data/transformed/"
refined_data = f"{dirname}/data/refined/"

df = pd.read_csv(f"{raw_data}sigsif_list_raw.csv")
print(df.head(10))

print(df.info())

# Set columns to transform formatting
column_numbers = [0, 1, 2, 5, 6]

for col in column_numbers:
    df.iloc[:, col] = df.iloc[:, col].astype(str).str.title()

print(df.head())

df.rename(columns={
    'PAIS': 'pais',
    "AREA": "área",
    "ESTABELECIMENTO": "estabelecimento",
    "DT_VALIDADE": "dt_validade",
    "DT_OCORRENCIA": "dt_ocorrencia",
    "DT_SUSPENSAO": "dt_suspensao"
    })