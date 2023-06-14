import pandas as pd

LATEST_RESULTS_PATH = "latest_lab_results.csv"

lab_result = pd.read_csv(LATEST_RESULTS_PATH, index_col=[0])

frequencies = lab_result.value_counts('itemid').to_frame()

common_lab_results = [exam_occurence.name for _, exam_occurence in frequencies.iterrows() if exam_occurence['count'] == 100]

filtered_lab_results = pd.DataFrame(index=lab_result.index, columns=lab_result.columns).iloc[:0]

for index, row in lab_result.iterrows():
   if row['itemid'] in common_lab_results:
      filtered_lab_results.loc[len(filtered_lab_results)] = row


patients_exams = pd.DataFrame(index=filtered_lab_results.index, columns=(['subject_id']+common_lab_results)).iloc[:0]

# TODO expand patients_exams dataframe to have the diseases columns to use in the model
# TODO add the patient id, exam results and diagnosed diseases to patients_exams dataframe