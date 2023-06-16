import pandas as pd

DATA_PATH = "../../mimic-iii-clinical-database-demo-1.4"
LATEST_RESULTS_PATH = "latest_lab_results.csv"
DIAGNOSES_PATH = f"{DATA_PATH}/DIAGNOSES_ICD.csv"

lab_result = pd.read_csv(LATEST_RESULTS_PATH, index_col=[0])
diagnoses = pd.read_csv(DIAGNOSES_PATH, index_col=[0])

# use value counts to count every occurence of a lab exam and put it into a dictionary
lab_res_frequencies = lab_result.value_counts('itemid').to_dict()

# iterate through the dictionary and get only the common ones between every patient
# you can use loc with a lambda function in the previous value_counts to filter the common 
# ones between every patient but it makes the code less readable and there's no significant 
# performance improvement
common_lab_results = [exam for exam, count in lab_res_frequencies.items() if count == 100]

# use value counts to get all the unique codes to a dict and convert the keys (codes) to a list
diagnoses_list = list(diagnoses.value_counts('icd9_code').to_dict().keys())

patients_exams = pd.DataFrame(index=[], columns=(['subject_id']+common_lab_results+diagnoses_list)).iloc[:0]

print(patients_exams)

for _, patient_diagnose in lab_result.iterrows():
    if not patients_exams.loc[patients_exams['subject_id'].item() == 10006]:
        patients_exams.loc[len(patients_exams.index)] = pd.Series(patients_exams.columns)

print(patients_exams)
        

# TODO expand patients_exams dataframe to have the diseases columns to use in the model