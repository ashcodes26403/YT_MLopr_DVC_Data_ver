import pandas as pd
import os

#Sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True) # creating the data directory

file_path = os.path.join(data_dir, 'data.csv') # defining the file path
df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")

