import pandas as pd
import os

FILEPATH = 'mimic-iii-clinical-database-demo-1.4'

common_columns = {}

for filename in os.scandir(FILEPATH):
    if filename.is_file:
        file = pd.read_csv(filename.path, low_memory=False)
        for column in file.columns:
            if column not in common_columns:    
                common_columns[column] = ""
            common_columns[column] += f"{filename.name}, "



df = pd.DataFrame(common_columns.items(), columns=["columns","files"])

df.to_csv('common_columns_in_files.csv')