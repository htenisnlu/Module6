import math

# Hikmet Tenis
# 08/10/2024
# The program converts a value in radians to degrees and compares it to the math.degrees function

# Function to convert radians to degrees
def radians_to_degrees(radians):
    return radians * (180 / math.pi)

# Get user input for radians
radians_input = float(input("Enter the value in radians: "))

# Convert radians to degrees using the custom function
custom_degrees = radians_to_degrees(radians_input)

# Convert radians to degrees using the math module
math_degrees = math.degrees(radians_input)

# Print the results
print("Converted value using custom function: {:.2f} degrees".format(custom_degrees))
print("Converted value using math.degrees function: {:.2f} degrees".format(math_degrees))
