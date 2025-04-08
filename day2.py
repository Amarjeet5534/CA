import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r'C:\Users\ar941\Downloads\Flight_Price_Dataset_of_Bangladesh.csv')
df.head()
# Clean the data (remove rows with missing values in key columns)
df_clean = df.dropna(subset=["Airline", "Total Fare (BDT)"])

# Group by airline and calculate statistics
airline_fare_stats = df_clean.groupby("Airline")["Total Fare (BDT)"].agg(["mean", "count", "min", "max"]).sort_values(by="mean")

# Print the top 5 cheapest and most expensive airlines
print("Top 5 Cheapest Airlines:")
print(airline_fare_stats.head(5)[["mean"]])
print("\nTop 5 Most Expensive Airlines:")
print(airline_fare_stats.tail(5)[["mean"]])

# Plot average fare by airline
plt.figure(figsize=(12, 6))
airline_fare_stats["mean"].plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Fare by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Total Fare (BDT)")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()

# Save the plot to file
plt.savefig("Average_Fare_by_Airline.png")
plt.show()
