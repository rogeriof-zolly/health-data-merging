import numpy as np
np.random.seed(1377)
import random as rn
rn.seed(1254)
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras import layers
from tensorflow import get_logger
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
get_logger().setLevel('ERROR')


DATA_PATH = "../../mimic-iii-clinical-database-demo-1.4"
LATEST_RESULTS_PATH = "latest_lab_results.csv"
DIAGNOSES_PATH = f"{DATA_PATH}/DIAGNOSES_ICD.csv"

patients = pd.read_csv("../data_treatment/patients_database.csv")
diag = pd.read_csv(DIAGNOSES_PATH)
frequent_diseases = list(diag.value_counts('icd9_code').loc[lambda occur: occur > 47].to_dict().keys())

# variables to keep each learning iteration's loss score and accuracy
score, accuracy = 1, 0

# get the inputs and outputs from the patients database
x = pd.get_dummies(patients.drop(['Unnamed: 0', 'subject_id']+list(patients.columns[22:]), axis=1))
y = patients[frequent_diseases]

# while the accuracy is below 0.8 and the loss score is above 1
# keep updating the training inputs until the condition is met
while (score >= 1 or accuracy < 0.8):

  X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, 
    train_size=0.8, 
    test_size=0.2,
    shuffle=False, 
    stratify=None,
  )

  model = Sequential([
    layers.Dense(4, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(2,activation='sigmoid')
  ])
  model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

  model.fit(X_train, Y_train, epochs=11, shuffle=False)

  score, accuracy = model.evaluate(X_test, Y_test)

# prints the final scores
print('Final score:', score)
print('Final accuracy:', accuracy)