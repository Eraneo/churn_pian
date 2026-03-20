print ("Analysing customer churn with random forest")

import pandas as pd

# import dataset
data = pd.read_csv("https://raw.githubusercontent.com/Eraneo/churn_pian/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print (data.info())

print (data["TotalCharges"].head())
# kedepannya kudu labelencoder untuk TotalCharges karena masih string