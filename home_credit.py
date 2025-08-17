#Loan Default Prediction - BeastAJ

## Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

# Download latest version
path = kagglehub.dataset_download("julianocosta/home-credit")

//print("Path to dataset files:", path)

## Step 2: Load Dataset
# Replace the path with your actual dataset path
train = pd.read_csv(path)

## Step 3: Basic Overview
print(train.shape)
print(train.head())

## Step 4: Target Variable Distribution
sns.countplot(x='TARGET', data=train)
plt.title('Default vs Non-Default Distribution')
plt.show()

# Check class balance
print(train['TARGET'].value_counts(normalize=True))

## Step 5: Missing Values Overview
missing = train.isnull().sum() / len(train) * 100
missing = missing[missing > 0].sort_values(ascending=False)
print(missing.head(20))

sns.barplot(x=missing.values[:20], y=missing.index[:20])
plt.title('Top 20 Missing Values (%)')
plt.show()

## Step 6: Data Types & Basic Info
print(train.info())

## Step 7: Save Data Dictionary
data_dict = pd.DataFrame({
    'Column': train.columns,
    'DataType': train.dtypes.values,
    'MissingPct': train.isnull().sum().values / len(train) * 100
})
data_dict.to_csv('data_dictionary.csv', index=False)
print('Data dictionary saved as data_dictionary.csv')
