import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data
Time = np.array([6, 8, 11, 14, 16, 18, 19])
Temp = np.array([4, 7, 10, 12, 11.5, 9, 7])

# Data Exploration
print("Descriptive Statistics for Temperature:")
print(f"Mean: {np.mean(Temp)}")
print(f"Median: {np.median(Temp)}")
print(f"Standard Deviation: {np.std(Temp)}")

# Check for missing values
if np.isnan(Temp).any() or np.isnan(Time).any():
    print("Warning: Missing data detected!")
else:
    print("No missing data.")

# Initial Plot
plt.figure(figsize=(10, 6))
plt.plot(Time, Temp, 'bo', label='Observed Data')
plt.xlabel("Time")
plt.ylabel("Temp")
plt.title('Temperature versus Time')
plt.grid(True)

# Highlighting max and min temperatures
max_temp_idx = np.argmax(Temp)
min_temp_idx = np.argmin(Temp)
plt.scatter(Time[max_temp_idx], Temp[max_temp_idx], color='red', label='Max Temp')
plt.scatter(Time[min_temp_idx], Temp[min_temp_idx], color='green', label='Min Temp')

plt.legend()

# Polynomial Fit
degree = 2
beta = np.polyfit(Time, Temp, degree)
p = np.poly1d(beta)

# Plotting the polynomial fit
xp = np.linspace(6, 19, 100)
plt.plot(xp, p(xp), '-', label=f'{degree}-Degree Polynomial Fit')

# Display the equation
plt.text(6, 4, f'Fit Equation: {p}', fontsize=9)

# Calculate and display R-squared
yhat = p(Time)
SS_res = np.sum((Temp - yhat) ** 2)
SS_tot = np.sum((Temp - np.mean(Temp)) ** 2)
r_squared = 1 - (SS_res / SS_tot)
plt.text(6, 3.5, f'R-squared: {r_squared:.3f}', fontsize=9)

plt.legend()
plt.show()
