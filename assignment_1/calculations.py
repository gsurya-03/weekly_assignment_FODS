# Take input from user for two numbers
a = int(input("Enter first number "))
b = int(input("Enter second number "))

# Calculate and display sum of two numbers
print(f"The sum of {a} and {b} is ", a + b)

# Calculate and display product of two numbers
print(f"The product of {a} and {b} is ", a * b)

# Division logic
# Check which number is greater and divide larger by smaller
if a > b:
    div = a / b
    print(f"The division of {a} and {b} is ", div)

elif b > a:
    div = b / a
    print(f"The division of {b} and {a} is", div)

# Modulus logic
# Find remainder when larger number is divided by smaller
if a > b:
    mod = a % b
    print(f"The modulus of {a} % {b} is", mod)

elif b > a:
    mod = b % a
    print(f"The modulus of {b} % {a} is", mod)

# Exponentiation
# Raise a to the power of b
print(f"The exponentiation of {a}^{b} is ", a ** b)