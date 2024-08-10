import math

# Hikmet Tenis
# 08/10/2024
# The program approximates the value of pi using the Leibniz formula and compares it to math.pi

def calculate_pi_approximation(n_terms):
    approximation = 0
    for i in range(n_terms):
        term = (-1) ** i / (2 * i + 1)
        approximation += term
    return 4 * approximation

# Number of terms to use in the approximation
n_terms = 1000000

# Calculate the approximation of pi
pi_approximation = calculate_pi_approximation(n_terms)

# Print the approximated value and the actual value from the math module
print("Approximated value of pi:", pi_approximation)
print("Value of math.pi:", math.pi)