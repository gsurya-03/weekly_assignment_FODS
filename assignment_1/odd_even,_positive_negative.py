# Use exception handling to prevent garbage input errors
# try block runs the code and except handles invalid input
try:
    # Take integer input from user
    a = int(input("Enter a number "))  

    # Special case when input is zero
    # Zero is neither positive nor negative and is even
    if a == 0:
        print(f"This is {a} Please enter a number other than 0")

    # Check if number is positive
    if a > 0:
        print(f"{a} is a positive number")
    
    # Check if number is even
    elif a % 2 == 0:
        print(f"{a} is even")
    
    # Check if number is positive odd
    elif a > 0 and a % 2 == 1:
        print(f"{a} is a positive odd number")
    
    # Check if number is negative
    elif a < 0:
        print(f"{a} is a negative number")
    
    # Check if number is negative odd
    elif a < 0 and a % 2 == 1:
        print(f"{a} is a negative odd number")

# Handle invalid input like string or symbols
except ValueError:
    print("Invalid input Please enter a number")