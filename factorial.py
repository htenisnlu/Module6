import math

# Hikmet Tenis
# 08/10/2024
# This program calculates the factorial of a user input value using a for loop and compares it to the value calculated by math.factorial

# Function to calculate factorial using a for loop
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Get user input for the number
number = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial using the custom function
custom_factorial = calculate_factorial(number)

# Calculate factorial using the math module
math_factorial = math.factorial(number)

# Print the results
print("Factorial calculated using custom function: {}".format(custom_factorial))
print("Factorial calculated using math.factorial function: {}".format(math_factorial))