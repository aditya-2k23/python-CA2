# 🎮 Video Game Sales Analysis

## 📌 Problem Statement

Understanding the key factors that influence video game sales across regions, platforms, genres, and time by analyzing critic scores, publisher impact, and release patterns to uncover trends that drive commercial success in the gaming industry.

For better visualizations check out the jupyter notebook here [Jupyter Notebook](https://www.github.com/aditya-2k23/python-CA2/blob/main/jupyter-analysis.ipynb) 

## 📊 Objectives

Platform vs Region
Identify which platforms perform best in different regions using regional sales data.

Top Genres by Region
Analyze genre preferences across regions to determine which types of games are most popular where.

Publisher and Developer Influence
Evaluate the impact of game publishers and developers on critic ratings and sales performance.

Critic Scores vs Sales
Assess whether critic reviews have a measurable influence on total game sales.

## 🛠️ Methodology

Data Preprocessing
Dataset imported from Excel (dataset.xlsx)
Handled missing values, dropped irrelevant columns, and parsed release dates
Outliers detected using Z-Score method
Dataset limited to top 5000 entries for efficiency
Exploratory Data Analysis (EDA)
Summary statistics and structural overview of dataset
Missing values and duplicates inspection
Correlation heatmap for numerical features

## 📈 Analysis Breakdown

### 1. Platform Performance by Region
Total regional sales computed for top platforms
Stacked bar chart visualizes how different consoles perform across North America, Japan, PAL, and Other regions

### 2. Genre Popularity by Region
Sales aggregated by genre across each region
Bar charts and heatmaps illustrate regional preferences
Additional breakdown of global vs regional performance of each genre

### 3. Publisher and Developer Impact
Top 15 publishers ranked by average critic score
Top 15 developers ranked by average total game sales
Visualized with bar charts

### 4. Critic Scores and Sales
Critic scores binned into intervals
Average sales per score bin analyzed
Assessed impact of critical reception on commercial success

## 🧪 Tools & Libraries
- Python
- Pandas, NumPy – Data manipulation
- Matplotlib, Seaborn – Data visualization

## 📌 Conclusion
The analysis provides insights into:
- Regional strengths of different gaming platforms
- Genre popularity across continents
- Influence of publishers and developers on game performance
- The role of critic scores in predicting sales success

These findings can assist game developers, marketers, and publishers in making data-driven decisions to optimize game design, marketing strategies, and platform targeting.
