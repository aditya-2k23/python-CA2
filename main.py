# Problem statement
"""
Video Game Sales: Understanding the key factors that influence game sales across regions, platforms, genres, and time by analyzing critic scores, publisher impact, and release patterns to uncover trends that drive commercial success in the gaming industry.
"""

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

# Handling missing values
df = df.drop(columns=['last_update'])

# Handling missing values in the 'year_of_release' column
sales_columns = ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']
df[sales_columns] = df[sales_columns].fillna(0)

# Dropping rows with missing values in 'critic_score'
df_critic = df.dropna(subset=['critic_score'])

# Extracting the year and month from 'relase_date'
df['release_year'] = pd.to_datetime(df['release_date']).dt.year
df['release_month'] = pd.to_datetime(df['release_date']).dt.month

# Keep only the relevant columns
key_columns = ['title', 'console', 'genre', 'publisher', 'developer', 'critic_score', 'release_date', 'release_year', 'release_month'] + sales_columns

clean_df = df[key_columns]
