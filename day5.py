import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r'C:\Users\ar941\Downloads\Flight_Price_Dataset_of_Bangladesh.csv')
df.head()
# Convert the departure datetime column
df["Departure Date & Time"] = pd.to_datetime(df["Departure Date & Time"], errors='coerce')

# Drop rows with missing datetime or fare
df = df.dropna(subset=["Departure Date & Time", "Total Fare (BDT)"])

# Define a function to categorize time of day
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

# Apply the time-of-day categorization
df["Time of Day"] = df["Departure Date & Time"].dt.hour.apply(get_time_of_day)

# Calculate average fare by time of day
time_of_day_fare = df.groupby("Time of Day")["Total Fare (BDT)"].mean().sort_values()

# Plot the results
plt.figure(figsize=(8, 5))
plt.bar(time_of_day_fare.index, time_of_day_fare.values, color="skyblue", edgecolor="black")
plt.title("Average Flight Fare by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Average Fare (BDT)")
plt.grid(axis="y")
plt.tight_layout()

# Save the plot
plt.savefig("Flight_Fare_By_Time_of_Day.png")
plt.show()
