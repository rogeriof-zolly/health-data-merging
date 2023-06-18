import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras import layers
from sklearn.metrics import accuracy_score

DATA_PATH = "../../mimic-iii-clinical-database-demo-1.4"
LATEST_RESULTS_PATH = "latest_lab_results.csv"
DIAGNOSES_PATH = f"{DATA_PATH}/DIAGNOSES_ICD.csv"

patients = pd.read_csv("../data_treatment/patients_database.csv")
diag = pd.read_csv(DIAGNOSES_PATH)
frequent_diseases = list(diag.value_counts('icd9_code').loc[lambda occur: occur > 47].to_dict().keys())

x = pd.get_dummies(patients.drop(['Unnamed: 0', 'subject_id']+list(patients.columns[22:]), axis=1))
y = patients[frequent_diseases]

X_train, X_test, Y_train, Y_test = train_test_split(x, y, train_size=0.5, test_size=0.5)

model = Sequential([
  layers.Dense(32, activation='relu'),
  layers.Dense(64, activation='relu'),
  layers.Dense(128, activation='relu'),
  layers.Dense(512, activation='relu'),
  layers.Dense(1024, activation='relu'),
  layers.Dense(512, activation='relu'),
  layers.Dense(256, activation='relu'),
  layers.Dense(2,activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

model.fit(X_train, Y_train, epochs=1000)

score, accuracy = model.evaluate(X_test, Y_test)
print('score:', score)
print('accuracy:', accuracy)