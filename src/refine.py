import pandas as pd
import os

# Set directory folders to store our data
dirname = os.getcwd()

raw_data = f"{dirname}/data/raw/"
transformed_data = f"{dirname}/data/transformed/"
refined_data = f"{dirname}/data/refined/"

df = pd.read_csv(f"{transformed_data}sigsif_list_transformed.csv")

df.to_excel(f"{refined_data}sigsif_list_refined.xlsx", sheet_name="Habilitação SIF por País", header=1, index=False)