import pandas as pd
import os

# Set directory folders to store our data
dirname = os.getcwd()

raw_data = f"{dirname}/data/raw/"
transformed_data = f"{dirname}/data/transformed/"
refined_data = f"{dirname}/data/refined/"

df = pd.read_csv(f"{raw_data}sigsif_list_raw.csv")


# Set columns to transform formatting
column_numbers = [0, 1, 2, 5, 6]

for col in column_numbers:
    df.iloc[:, col] = df.iloc[:, col].astype(str).str.title()


df = df.rename(columns={
    'PAIS': 'pais',
    "AREA": "area",
    "ESTABELECIMENTO": "estabelecimento",
    "MUNICIPIO": "municipio",
    "PRODUTO": "produto",
    "DT_VALIDADE": "dt_validade",
    "DT_OCORRENCIA": "dt_ocorrencia",
    "DT_SUSPENSAO": "dt_suspensao"
    })

# Change dtypes
date_cols = ["dt_validade", "dt_ocorrencia", "dt_suspensao"]
df[date_cols] = df[date_cols].apply(pd.to_datetime, errors="coerce").apply(lambda x: x.dt.date)
print(df.info())

df.to_csv(f"{transformed_data}sigsif_list_transformed.csv", sep=",", index=False)