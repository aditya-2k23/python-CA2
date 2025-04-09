# Problem statement
"""
Video Game Sales: Understanding the key factors that influence game sales across regions, platforms, genres, and time by analyzing critic scores, publisher impact, and release patterns to uncover trends that drive commercial success in the gaming industry.
"""

import numpy as np
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

# Extracting the year and month from 'release_date'
df['release_year'] = pd.to_datetime(df['release_date']).dt.year
df['release_month'] = pd.to_datetime(df['release_date']).dt.month

# Keep only the relevant columns
key_columns = ['title', 'console', 'genre', 'publisher', 'developer', 'critic_score', 'release_date', 'release_year', 'release_month'] + sales_columns

clean_df = df[key_columns]

df = df.head(1000).copy()

#? Outlier Detection using z_score

# Step 1: Select numeric columns for outlier detection
numeric_cols = ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales', 'critic_score']

# Step 2: Drop rows with missing critic_score
df_z = clean_df.dropna(subset=['critic_score'])

# Step 3: Calculate z-scores manually
z_scores = (df_z[numeric_cols] - df_z[numeric_cols].mean()) / df_z[numeric_cols].std()

# Step 4: Set threshold and detect outliers
threshold = 3
outliers = (np.abs(z_scores) > threshold).any(axis=1)

# Step 5: Count and show outliers
print(f"Number of outliers found: {outliers.sum()}")

# !1. Platform vs Region — Which platform performs better where? by analyzing the sales data by platform and region.

# List of popular consoles
popular_consoles = ["PS", "PS2", "PS3", "PS4", "PS5", "XONE", "X360",
                    "PC", "PSP", "Wii", "DS", "XB", "GBA", "GC", "2600", "N64"]

# Filter the dataset to only keep rows where console is in the popular list
df_ready = clean_df[clean_df['console'].isin(popular_consoles)]

# Group by console and calculate the sum of sales for each region
region_sales = df_ready.groupby('console')[['na_sales', 'jp_sales', 'pal_sales', 'other_sales']].sum()

plt.figure(figsize=(12, 6))

# Create a bar plot for each region
sns.barplot(x=region_sales.index, y=region_sales['na_sales'], label='North America', color='blue', alpha=0.7)
sns.barplot(x=region_sales.index, y=region_sales['jp_sales'], label='Japan', color='red', alpha=0.7, bottom=region_sales['na_sales'])
sns.barplot(x=region_sales.index, y=region_sales['pal_sales'], label='PAL', color='green', alpha=0.7, bottom=region_sales['na_sales'] + region_sales['jp_sales'])
sns.barplot(x=region_sales.index, y=region_sales['other_sales'], label='Other', color='orange', alpha=0.7, bottom=region_sales['na_sales'] + region_sales['jp_sales'] + region_sales['pal_sales'])

plt.xticks(rotation=45)
plt.title('Regional Sales by Gaming Platform')
plt.xlabel('Gaming Platform')
plt.ylabel('Sales (in millions)')
plt.legend(title='Region')
plt.show()

# !2. Top Genres — Who loves what genre, and where? by analyzing the sales data by genre and region.

# Group by genre and calculate the sum of sales for each region
genre_sales = df_ready.groupby('genre')[['na_sales', 'jp_sales', 'pal_sales', 'other_sales']].sum()

# Sort the data by total sales (sum of all regions) in descending order
genre_sales['total_sales'] = genre_sales.sum(axis=1)
genre_sales = genre_sales.sort_values(by='total_sales', ascending=False)

plt.figure(figsize=(12, 6))

# Create a bar plot for each region
sns.barplot(x=genre_sales.index, y=genre_sales['na_sales'], label='North America', color='blue', alpha=0.7)
sns.barplot(x=genre_sales.index, y=genre_sales['jp_sales'], label='Japan', color='red', alpha=0.7, bottom=genre_sales['na_sales'])
sns.barplot(x=genre_sales.index, y=genre_sales['pal_sales'], label='PAL', color='green', alpha=0.7, bottom=genre_sales['na_sales'] + genre_sales['jp_sales'])
sns.barplot(x=genre_sales.index, y=genre_sales['other_sales'], label='Other', color='orange', alpha=0.7, bottom=genre_sales['na_sales'] + genre_sales['jp_sales'] + genre_sales['pal_sales'])

plt.xticks(rotation=45)
plt.title('Regional Sales by Genre')
plt.xlabel('Genre')
plt.ylabel('Sales (in millions)')
plt.legend(title='Region')
plt.show()


# ! Objective 3: To determine which genres are most appealing to consumers and where by analyzing total and regional sales figures by game genre like Action, Shooter, Sports.

# 1. Total Sales by Genre
total_sales_by_genre = df.groupby("genre")["total_sales"].sum().sort_values(ascending=False)

# 2. Regional Sales by Genre
regional_sales_by_genre = df.groupby("genre")[["na_sales", "jp_sales", "pal_sales", "other_sales"]].sum()

# Plotting Total Sales by Genre
plt.figure(figsize=(12, 6))
sns.barplot(x=total_sales_by_genre.values, y=total_sales_by_genre.index,hue=total_sales_by_genre.index, palette="viridis")
plt.title("Total Global Sales by Genre")
plt.xlabel("Total Sales (in millions)")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

# Plotting Regional Sales by Genre
# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(regional_sales_by_genre, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.5)
plt.title("Regional Sales Heatmap by Genre")
plt.xlabel("Region")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
