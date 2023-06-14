import pandas as pd
import os

FILEPATH = '../../mimic-iii-clinical-database-demo-1.4'
IGNORED_FILES = [
    'ADMISSIONS.csv', 
    'CALLOUT.csv',
    'CAREGIVERS.csv', 
    'DATETIMEEVENTS.csv', 
    'NOTEEVENTS.csv', 
    'PRESCRIPTIONS.csv',
    'PROCEDUREEVENTS_MV.csv',
    'SERVICES.csv',
    'TRANSFERS.csv',
    'CPTEVENTS.csv'
]

common_columns = {}

for filename in os.scandir(FILEPATH):
    if str(filename.name) not in IGNORED_FILES and filename.is_file:
        file = pd.read_csv(filename.path, low_memory=False)
        for column in file.columns:
            if column not in common_columns:    
                common_columns[column] = ""
            common_columns[column] += f"{filename.name}, "



df = pd.DataFrame(common_columns.items(), columns=["columns","files"])
df = df.sort_values(by="files", key=lambda file: file.str.len(), ascending=False)


df.to_csv('common_columns_in_files.csv')