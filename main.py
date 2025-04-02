import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("./dataset.xlsx")

"""EDA"""
print(df.head())
print(df.info())

print("Checking for missing values...")
print(df.isnull().sum())

print("Checking for duplicates:", end=" ")
print(df.duplicated().sum())
print("Summarizing the data:")
print(df.describe())
print("Columns in the dataset:")
print(df.columns.tolist())
