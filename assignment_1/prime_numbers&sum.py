# Take input from user for starting and ending range
a = int(input("Enter the starting number to start counting "))
b = int(input("Enter the number till you need counting "))

# Initialize variables to count primes and store their sum
count = 0
total = 0

# Display message about the operation
print(f"\n Counting prime number from {a} to {b}")

# Loop through each number in the given range
for i in range(a, b + 1):
    
    # Prime numbers are greater than 1
    if i > 1:
        
        # Assume number is prime initially
        is_prime = True

        # Check divisibility from 2 to square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            
            # If divisible then it is not prime
            if i % j == 0:
                is_prime = False
                break

        # If number is still marked as prime
        if is_prime:
            # Print the prime number
            print(i)
            
            # Increase count of prime numbers
            count += 1
            
            # Add to total sum of primes
            total += i

# Print final results
print(f"The prime numbers between {a} to {b} are ")
print(f"The sum of all prime numbers are ", total)