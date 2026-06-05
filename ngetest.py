print ("check")

import pandas as pd

# import dataset
data = pd.read_csv("https://raw.githubusercontent.com/Eraneo/churn_pian/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print (data.info())

print (data["TotalCharges"].head())
# kedepannya kudu labelencoder untuk TotalCharges karena masih string
print (data)
binary_cols = [
    'gender',
    'Partner',
    'Dependents',
    'PhoneService',
    'PaperlessBilling',
    'Churn'
]

for col in binary_cols:
    data[col] = data[col].map({
        'Yes':1, 'No':0,
        'Male':1, 'Female':0
    })