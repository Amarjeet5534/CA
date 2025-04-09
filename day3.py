import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\ar941\Downloads\Flight_Price_Dataset_of_Bangladesh.csv')
#df.head()

# Create a "Route" column by combining Source and Destination
df["Route"] = df["Source"] + " → " + df["Destination"]

# Drop rows with missing values in required columns
df_clean = df.dropna(subset=["Airline", "Route", "Class", "Total Fare (BDT)"])

#Group by Airline, Route, and Class to calculate average fare
class_fare_stats = df_clean.groupby(["Airline", "Route", "Class"])["Total Fare (BDT)"].mean().reset_index()

# Find routes that offer more than one travel class (for fair comparison)
route_class_counts = class_fare_stats.groupby(["Airline", "Route"])["Class"].nunique().reset_index()
common_routes = route_class_counts[route_class_counts["Class"] > 1][["Airline", "Route"]]

# Filter original stats to only include routes with multiple classes
comparison_df = class_fare_stats.merge(common_routes, on=["Airline", "Route"])

# Display a preview of the comparison
print("Sample comparison of average fares across classes for same airline and route:\n")
print(comparison_df.sort_values(by=["Airline", "Route", "Class"]).head(15))
