# health-data-merging
This is a college work for the Advanced Artificial Intelligence discipline to develop on neural networks. The idea is to use health data from PhysioNet repository to analyse patients' exams and pass them through a neural network that should give the correct illness as output. This project aims to treat the data and create a ML model with Tensorflow

# requirements
access to the MIMIC-III Clinical Database demo files from PhysioNet available at https://physionet.org/content/mimiciii-demo/1.4/ (must ask for credentials at the website)
python 3.10
pandas
tensorflow2

# how to get the model running

1- Download the MIMICIII database in the website after getting access to it
2- Paste the folder with the CSVs at the root of the project
3- The script number 1 is totally optional, it just gets what columns are used in each files
4- Run the script number 2 to get the latest lab results from the patients
5- Run the script number 3 to get the database to be used in training and testing the model with tensorflow
6- Run the script at src/model_training/training.py to run the training and testing of the model
