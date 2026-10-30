import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv(r"C:\Users\okoli\Desktop\books_data_cleaned.csv")

print("Data loaded successfully!")
print(df.head())
print("\nTotal books:", len(df))

# Set style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ============================================
# Chart 1: Number of Books by Rating
# ============================================
plt.figure()
sns.countplot(data=df, x="Rating", palette="viridis")
plt.title("Number of Books by Rating", fontsize=16)
plt.xlabel("Rating (1-5)")
plt.ylabel("Number of Books")
plt.savefig("chart1_books_by_rating.png", dpi=300, bbox_inches="tight")
plt.show()

# ============================================
# Chart 2: Average Price by Rating
# ============================================
plt.figure()
sns.barplot(data=df, x="Rating", y="Price", palette="magma", errorbar=None)
plt.title("Average Book Price by Rating", fontsize=16)
plt.xlabel("Rating (1-5)")
plt.ylabel("Average Price (£)")
plt.savefig("chart2_avg_price_by_rating.png", dpi=300, bbox_inches="tight")
plt.show()

# ============================================
# Chart 3: Distribution of Book Prices
# ============================================
plt.figure()
sns.histplot(data=df, x="Price", bins=20, kde=True, color="teal")
plt.title("Distribution of Book Prices", fontsize=16)
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("chart3_price_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# ============================================
# Chart 4: Box Plot of Price by Rating
# ============================================
plt.figure()
sns.boxplot(data=df, x="Rating", y="Price", palette="coolwarm")
plt.title("Book Price Distribution by Rating", fontsize=16)
plt.xlabel("Rating (1-5)")
plt.ylabel("Price (£)")
plt.savefig("chart4_price_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nAll charts have been created and saved as PNG files!")
