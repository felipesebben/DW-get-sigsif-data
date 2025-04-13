import pandas as pd
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()
url = os.environ.get('URL')


# Create directory folders to store our data
dirname = os.getcwd()

raw_data = f"{dirname}/data/raw/"
transformed_data = f"{dirname}/data/transformed/"
refined_data = f"{dirname}/data/refined/"

paths = [raw_data, transformed_data, refined_data]

for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)


# Read .csv file
df = pd.read_csv(url,delimiter=";")
print(df.head())

# Store as raw file
df.to_csv(f"{raw_data}sigsif_list_raw.csv", sep=',', index=False)
