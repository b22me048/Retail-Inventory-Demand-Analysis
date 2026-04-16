# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (public CSV)
url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"
df = pd.read_csv(url)

# NOTE:
# This is a retail-like dataset substitute (books sales proxy)

# Data Cleaning
df = df.dropna()

# Basic Info
print(df.head())
print(df.info())

# Analysis 1: Top Authors (Demand proxy)
top_authors = df['authors'].value_counts().head(10)

plt.figure()
top_authors.plot(kind='bar')
plt.title("Top Authors by Number of Books")
plt.xlabel("Author")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Analysis 2: Ratings Distribution
plt.figure()
sns.histplot(df['average_rating'], bins=20)
plt.title("Ratings Distribution")
plt.show()

# Analysis 3: Year-wise Books Published
df['original_publication_year'] = df['original_publication_year'].astype(int)

yearly = df['original_publication_year'].value_counts().sort_index()

plt.figure()
yearly.plot()
plt.title("Books Published Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()