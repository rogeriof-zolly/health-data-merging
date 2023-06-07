FILEPATH = 'mimic-iii-clinical-database-demo-1.4'

import pandas as pd
import os

file = pd.read_csv(f'{FILEPATH}/ADMISSIONS.csv')
dictionary = {}

for filename in os.scandir(FILEPATH):
    if filename.is_file:
        file = pd.read_csv(filename.path, low_memory=False)
        for col in file.columns:
            dictionary[col].append(filename.path)

print(dictionary)

""" dictionary = {}

for column, number in file.iterrows():
    dictionary[column] = [number]

print(dictionary)

df = pd.DataFrame(dictionary)

df.to_csv('arquivo.csv') """