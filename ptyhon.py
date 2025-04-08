import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r'C:\Users\ar941\Downloads\Flight_Price_Dataset_of_Bangladesh.csv')
df.head()



# Drop rows with missing values in relevant columns
df_clean = df.dropna(subset=["Days Before Departure", "Total Fare (BDT)"])

# Extract values
x = df_clean["Days Before Departure"]
y = df_clean["Total Fare (BDT)"]

# 1. Correlation using pandas
correlation = x.corr(y)

# 2. Manual Linear Regression using numpy
x_vals = x.values
y_vals = y.values
x_mean = np.mean(x_vals)
y_mean = np.mean(y_vals)

# Calculate slope (m) and intercept (b)
m = np.sum((x_vals - x_mean) * (y_vals - y_mean)) / np.sum((x_vals - x_mean) ** 2)
b = y_mean - m * x_mean

# Predict values and calculate R-squared
y_pred = m * x_vals + b
ss_total = np.sum((y_vals - y_mean) ** 2)
ss_res = np.sum((y_vals - y_pred) ** 2)
r_squared = 1 - (ss_res / ss_total)

# 3. Plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5, label='Actual Data')
plt.plot(x_vals, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title("Total Fare vs. Days Before Departure")
plt.xlabel("Days Before Departure")
plt.ylabel("Total Fare (BDT)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("fare_vs_days.png")
plt.show()

# 4. Print Results
print("Correlation Coefficient:", round(correlation, 4))
print("Regression Equation: Total Fare = {:.2f} - {:.2f} × Days Before Departure".format(b, abs(m)))
print("R-squared:", round(r_squared, 4))
