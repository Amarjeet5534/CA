import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\ar941\Downloads\Flight_Price_Dataset_of_Bangladesh.csv')
df.head()


# Create a Route column
df["Route"] = df["Source"] + " → " + df["Destination"]

# Clean the data
df_clean = df.dropna(subset=["Route", "Total Fare (BDT)"])

# Calculate average, min, max, and count fare per route
route_fare_stats = df_clean.groupby("Route")["Total Fare (BDT)"].agg(["mean", "count", "min", "max"]).sort_values(by="mean", ascending=False)

# Select top 10 most expensive routes
top_expensive_routes = route_fare_stats.head(10)

# Plot average fare for top 10 most expensive routes
plt.figure(figsize=(12, 6))
plt.bar(top_expensive_routes.index, top_expensive_routes["mean"], color="salmon", edgecolor="black")
plt.title("Top 10 Most Expensive Flight Routes (Average Fare in BDT)")
plt.ylabel("Average Fare (BDT)")
plt.xlabel("Route")
plt.xticks(rotation=45, ha='right')
plt.grid(axis="y")
plt.tight_layout()

# Save plot
plt.savefig("Top_10_Expensive_Routes.png")
plt.show()
