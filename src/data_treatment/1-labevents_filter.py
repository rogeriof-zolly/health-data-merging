import pandas as pd

DATA_PATH = "../../mimic-iii-clinical-database-demo-1.4"
LABEVENTS_FILE_PATH = f"{DATA_PATH}/LABEVENTS.csv"

labevents = pd.read_csv(LABEVENTS_FILE_PATH)

latest_results = labevents.sort_values(['subject_id', 'charttime']).groupby(['subject_id', 'itemid']).tail(1)

latest_results.to_csv('latest_lab_results.csv')