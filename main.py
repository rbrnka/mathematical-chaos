import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
num_iterations = 50
r_values = np.linspace(0, 4, 500)  # Range of r values for oscillation diagram

# Function 1
def function1(p, r):
    return p + r * p * (1 - p)

# Function 2
def function2(p, r):
    return (1 + r) * p - r * p**2

# Initial conditions
p0 = 0.01
r = 3

# Perform calculations for both functions
p_values_func1 = [p0]
p_values_func2 = [p0]

for _ in range(num_iterations - 1):
    p_next_func1 = function1(p_values_func1[-1], r)
    p_next_func2 = function2(p_values_func2[-1], r)
    p_values_func1.append(p_next_func1)
    p_values_func2.append(p_next_func2)

# Calculate the difference between the two functions
p_difference = [abs(f1 - f2) for f1, f2 in zip(p_values_func1, p_values_func2)]

# Create a DataFrame to display the results in a table
comparison_table = pd.DataFrame({
    "Function 1": p_values_func1,
    "Function 2": p_values_func2,
    "Diff": p_difference
})

# Display the table
print("Comparison of Calculations:")
print(comparison_table)
# display(styled_table) # or display styled

# Oscillation diagram (Bifurcation diagram) for Function 1
p_final_values = []
for r in r_values:
    p = p0
    # Iterate to let the system stabilize
    for _ in range(100):
        p = function1(p, r)
    # Collect the final values for oscillation
    for _ in range(30):
        p = function1(p, r)
        p_final_values.append((r, p))

# Convert to numpy array for easy handling
p_final_values = np.array(p_final_values)

# Plot the oscillation diagram
plt.figure(figsize=(12, 6))
plt.scatter(p_final_values[:, 0], p_final_values[:, 1], s=0.1, color="blue")
plt.title("Oscillation Diagram (Bifurcation) for Function 1")
plt.xlabel("r Value")
plt.ylabel("p Value")
plt.grid()
plt.show()

# Lyapunov Exponent Calculation
lyapunov_exponents = []
for r in r_values:
    p = 0.01
    lyapunov_sum = 0
    for _ in range(1000):
        p = function1(p, r)
        derivative = abs(1 + r - 2 * r * p)  # Derivative of the logistic map
        if derivative > 0:
            lyapunov_sum += np.log(derivative)
    lyapunov_exponents.append(lyapunov_sum / 1000)

# Plot Lyapunov Exponent
plt.figure(figsize=(12, 6))
plt.plot(r_values, lyapunov_exponents, color="green")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Lyapunov Exponent vs r")
plt.xlabel("r Value")
plt.ylabel("Lyapunov Exponent")
plt.grid()
plt.show()
