# Problem statement
"""
The video game industry is highly competitive, with numerous titles released across various consoles, genres, and regions. Companies need to understand the factors that contribute to a game's commercial success, critical reception, and regional market performance to optimize their development, marketing, and distribution strategies. Using the provided dataset, analyze the relationships between game attributes (e.g., genre, console, publisher, developer, critic score) and their sales performance (total and regional) to identify trends, patterns, and actionable insights that can guide decision-making in the gaming industry.
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
