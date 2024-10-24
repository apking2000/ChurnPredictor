import pickle
import os
import pandas as pd
from sklearn.metrics import recall_score, precision_score, accuracy_score
from config.config import CONFIG
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
# Setting the working directory

def main():
    # Explaintory vars
    final_df = pd.read_csv('~/'+CONFIG['data_path'])
    # Filter rows where 'Created_Date' matches the current date
    current_date = pd.Timestamp.now().normalize().date()
    final_df = final_df[final_df['Created_Date'] == str(current_date)]
    X = final_df.drop(['Churn Value','Created_Date'], axis = 1)
    # Target var
    Y = final_df['Churn Value']
    # Separating the dataset into train and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, 
                                                        test_size = 0.2, 
                                                        random_state = 1)
    xgb_model = XGBClassifier()
    xgb_model.fit(X_train, Y_train)

    # Accuracy score on training data
    xgb_train_pred = xgb_model.predict(X_train)
    xgb_acc_train = accuracy_score(xgb_train_pred, Y_train)
    # Accuracy score on test data
    xgb_test_pred = xgb_model.predict(X_test)
    xgb_acc_test = accuracy_score(xgb_test_pred, Y_test)
    ## recall,precision,accuracy
    xgb_recall = recall_score(Y_test,xgb_test_pred)
    xgb_precision = precision_score(Y_test, xgb_test_pred)
    print("XGBClassification model's metrics:\n")
    print("Accuracy on Training Data:", round(xgb_acc_train, 2))
    print("Accuracy on Test Data:", round(xgb_acc_test,2))
    print("Recall Score:", round(xgb_recall,2))
    print("Precision Score:", round(xgb_precision,2))

    # Save the model to a file
    with open(CONFIG['save_model_path'], 'wb') as file:
        pickle.dump(xgb_model, file)

if __name__ == '__main__':
    main()