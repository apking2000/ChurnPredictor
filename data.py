### Importing the libraries 
import kagglehub
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from config.config import CONFIG
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler

## data extraction
path = kagglehub.dataset_download("yeanzc/telco-customer-churn-ibm-dataset")
file_path = glob.glob(path+'/*')[0]

churn_df = pd.read_excel(file_path)

# Filter features
filtered_df = churn_df.iloc[:, 9:]
filtered_df.drop(['Gender','Total Charges','Churn Reason','Churn Label'], inplace = True, axis=1)

# Extract catagorical features from selected features 
cat_features = [i for i in filtered_df.columns if filtered_df[i].dtype == 'object']

# Encode cat_features
encoded_df = pd.get_dummies(filtered_df, columns = cat_features, drop_first = True)

# MinMax scaling of continous features 
scaler = MinMaxScaler()
temp_1 = scaler.fit_transform(filtered_df[["Tenure Months"]])

# Replacing the original cols with scaled ones 
encoded_df['Tenure Months'] = temp_1

feature_top7 = CONFIG['feature_top7']

top_feature_df = encoded_df[feature_top7]

## Treating the imbalance using upsampling technique
churned = top_feature_df[top_feature_df['Churn Value']==1]
not_churned = top_feature_df[top_feature_df['Churn Value'] == 0]

churned_upsampled = resample(churned, 
                             replace = True, 
                             n_samples = len(not_churned),
                             random_state = 1)

# Combining the upsampled data
final_df = pd.concat([churned_upsampled, not_churned])
final_df['Created_Date'] = pd.Timestamp.now().date()
final_df.to_csv("data.csv",index = False)