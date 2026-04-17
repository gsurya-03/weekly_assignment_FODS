# Display instruction for user
# The number should be positive
print("The number should be positive")

# Take input from user
n = int(input("Enter the number which you wanna find factorial of: "))

# Create a list to store numbers used in factorial
num = []

# Initialize output variable to store factorial result
output = 1

# Check if number is non negative
if n >= 0:
    
    # Loop from 1 to n to calculate factorial
    for i in range(1, n + 1):
        
        # Multiply each number to get factorial
        output *= i
        
        # Store numbers in list
        num.append(i)

    # Display the numbers used
    print(f"The numbers used are ", num)
    
    # Display the factorial result
    print(f"The factorial of {n} is ", output)

# If number is negative show error
elif n < 0:
    print("Invalid input Please enter a positive integer")

# Extra else for safety
else:
    print("Invalid input Please enter a positive integer")