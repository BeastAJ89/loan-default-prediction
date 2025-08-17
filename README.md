# loan-default-prediction
Predictor for probability of default in home loans

Problem: To predict the probabilty of default in Housing Loans

Dataset Source: Home Credit by JulianoCosta https://www.kaggle.com/datasets/julianocosta/home-credit/

Success Metrics:
  1. ROC-AUC >= 0.75
  2. recall for defaults >= 0.65

Checks to be done:
  1. Getting the dimensional measure of the dataset (Number of rows and columns)
  2. Defining our target variable - We are going to use 1 and 0 to indicate the status of the loan: 1 as default and 0 as repaid
  3. Missing value and cleaning the data
  4. Finding the imbalance of class
