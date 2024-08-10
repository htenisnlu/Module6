# Python Programs for Module 6: Lab Activity

This repository contains Python programs developed as part of Module 6: Lab Activity. Each program is designed to solve specific problems and demonstrate the use of various Python features and modules. Below are the details of each program, including their purpose, implementation, and example outputs.

---

### Problem 1: Generate Random Integers
**Description**: This program uses a `for` statement and `random.randrange` to print 10 random integers between 25 and 35.

```python
import random

for _ in range(10):
    print(random.randrange(25, 36))
```

**Example Output**:
```
29
33
25
35
27
32
26
30
28
34
```

---

### Problem 2: Generate an Odd Integer
**Description**: This program uses `random.randrange` to print an odd integer between 0 and 100.

```python
import random

print(random.randrange(1, 101, 2))
```

**Example Output**:
```
47
```

---

### Problem 3: Select a Day of the Week
**Description**: This program uses `random.choice` to select a day of the week from a list and print that day.

```python
import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(random.choice(days))
```

**Example Output**:
```
Thursday
```

---

### Problem 4: Approximate Pi
**Description**: This program calculates an approximation for pi using a simple arithmetic method and compares it with `math.pi`.

```python
import math

# Approximation of Pi using the Leibniz formula
def approximate_pi(n_terms):
    pi_approx = 0
    for k in range(n_terms):
        pi_approx += (-1)**k / (2*k + 1)
    return pi_approx * 4

# Calculate pi approximation
approx_pi = approximate_pi(1000000)
print("Approximate Pi:", approx_pi)
print("math.pi:", math.pi)
```

**Example Output**:
```
Approximate Pi: 3.1415916535897743
math.pi: 3.141592653589793
```

---

### Problem 5: Convert Radians to Degrees
**Description**: This program converts a user input value from radians to degrees and compares it with the result from the `degrees` function in the `math` module.

```python
import math

# Get user input for radians
radians = float(input("Enter the value in radians: "))

# Convert to degrees
degrees_manual = radians * (180 / math.pi)
degrees_math_module = math.degrees(radians)

# Print the results
print("Degrees (manual calculation):", degrees_manual)
print("Degrees (math.degrees function):", degrees_math_module)
```

**Example Output**:
```
Enter the value in radians: 1
Degrees (manual calculation): 57.29577951308232
Degrees (math.degrees function): 57.29577951308232
```

---

### Problem 6: Calculate Factorial
**Description**: This program calculates the factorial of a user input value using a `for` statement and compares it with the result from the `factorial` function in the `math` module.

```python
import math

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
print("Factorial calculated using custom function:", custom_factorial)
print("Factorial calculated using math.factorial function:", math_factorial)
```

**Example Output**:
```
Enter a number to calculate its factorial: 5
Factorial calculated using custom function: 120
Factorial calculated using math.factorial function: 120
```

