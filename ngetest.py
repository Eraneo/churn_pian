print ("check")

import pandas as pd

# import dataset
data = pd.read_csv("https://raw.githubusercontent.com/Eraneo/churn_pian/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print (data.info())
print (data["PaymentMethod"].value_counts())

# Ganti kategori data
data_copy = data.copy()
# data biner
binary_cols = [
    'gender',
    'Partner',
    'Dependents',
    'PhoneService',
    'PaperlessBilling',
    'Churn'
]

for col in binary_cols:
    data_copy[col] = data_copy[col].map({
        'Yes':1, 'No':0,
        'Male':1, 'Female':0
    })

# data kategorikal
data_copy = pd.get_dummies(
    data_copy,
    columns=[
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaymentMethod'
    ],
    drop_first=True
)

# data numerik
data_copy['TotalCharges'] = pd.to_numeric(data_copy['TotalCharges'], errors='coerce')

print (data_copy.info())
print (data_copy.head())