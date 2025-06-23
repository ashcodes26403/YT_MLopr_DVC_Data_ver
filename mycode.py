import pandas as pd
import os

#Sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

new_row_loc = {'Name': 'Doe', 'Age': 40, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row_loc

new_row_loc_2 = {'Name': 'Eve', 'Age': 45, 'City': 'Tokyo'}
df.loc[len(df.index)] = new_row_loc_2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True) # creating the data directory

file_path = os.path.join(data_dir, 'data.csv') # defining the file path
df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")

