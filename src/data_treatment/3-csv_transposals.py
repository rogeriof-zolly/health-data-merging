import pandas as pd

DATA_PATH = "../../mimic-iii-clinical-database-demo-1.4"
LATEST_RESULTS_PATH = "latest_lab_results.csv"
DIAGNOSES_PATH = f"{DATA_PATH}/DIAGNOSES_ICD.csv"

lab_result = pd.read_csv(LATEST_RESULTS_PATH, index_col=[0])
diagnoses = pd.read_csv(DIAGNOSES_PATH, index_col=[0])

# use value counts to count every occurence of a lab exam and put it into a dictionary
lab_res_frequencies = lab_result.value_counts('itemid').to_dict()

# iterate through the dictionary and get only the common ones between every patient
common_lab_results = [exam for exam, count in lab_res_frequencies.items() if count == 100]

# update lab_result with only the common exams
lab_result = lab_result.loc[lab_result['itemid'].isin(common_lab_results)]

# use value counts to get all the unique codes to a dict and convert the keys (codes) to a list
diagnoses_list = list(diagnoses.value_counts('icd9_code')
                      .loc[lambda numDiagnostics: numDiagnostics > 47]
                      .to_dict().keys())
patients_codes = list(diagnoses.value_counts('subject_id').to_dict().keys())

# create a dataframe to create the database
patients_db = pd.DataFrame(index=range(100), columns=(['subject_id']+common_lab_results+diagnoses_list))

# populate the dataframe with one patient for each row
for idx, patient in patients_db.iterrows():
    patient['subject_id'] = patients_codes[idx]


# iterate over the populated patients database
for idx, patient in patients_db.iterrows():
    # get the exams with the patient ID of that iteration
    patient_exams = lab_result.loc[lab_result['subject_id'] == patient['subject_id']]

    # get the diagnoses with the patient ID of that iteration
    patient_diagnoses = diagnoses.loc[diagnoses['subject_id'] == patient['subject_id']]

    # fill the patient's row with the exams results
    for _, exams in patient_exams.iterrows():
        patients_db.at[idx, exams['itemid']] = exams['value']

    # fill the patient's row with the diagnostics where it is positive
    for _, diagnostic in patient_diagnoses.iterrows():
        patients_db.at[idx, diagnostic['icd9_code']] = 1

# fill every blankspace with 0
patients_db = patients_db.fillna(0)

# export the database
patients_db.to_csv('patients_database.csv')