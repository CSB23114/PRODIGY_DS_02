import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('laptop_prices.csv')

# View the first few rows of the dataset
df.head()

# Check for missing values
df.isnull().sum()

# Check for duplicate rows
df.duplicated().sum()

# Drop duplicates if necessary
df = df.drop_duplicates()

df.info()

# If a column is in the wrong format (e.g., 'Price' as string), convert it
df['Price_euros'] = pd.to_numeric(df['Price_euros'], errors='coerce')

# Summary statistics
df.describe()

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of prices
plt.figure(figsize=(10,6))
sns.histplot(df['Price_euros'], kde=True)
plt.title('Distribution of Laptop Prices')
plt.show()

# Scatter plot of price vs. RAM
plt.figure(figsize=(10,6))
sns.scatterplot(x='Ram', y='Price_euros', data=df)
plt.title('Price_euros vs. Ram')
plt.show()

# Boxplot for price by brand
plt.figure(figsize=(12,6))
sns.boxplot(x='CPU_freq', y='Price_euros', data=df)
plt.title('Price Distribution by CPU_freq')
plt.xticks(rotation=90)
plt.show()

