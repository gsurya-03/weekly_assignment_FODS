# Ask the user to choose an option
a = int(input("Press 1 for default \n" \
          "Press 2 to enter the numbers of range 1000-2500 \n" \
          "\n Choose: "))

# Create an empty list to store results
num = []

# If user selects option 1 use default range 1000 to 2500
if a == 1:
    # Loop through numbers from 1000 to 2500
    for i in range(1000, 2501):
        # Check if number is divisible by 9 but not divisible by 6
        if i % 9 == 0 and i % 6 != 0:
            # Add number to list
            num.append(i)

    # Display the result
    print("The numbers between 1000-2500 that are divisible by 9 but not by 6 are")
    print(num)

# If user selects option 2 allow custom range input
elif a == 2:
    # Take range input in format start-end
    range_input = input("Enter the range format start-end ")
    
    # Split the input into start and end values
    start_str, end_str = range_input.split("-")
    
    # Convert string values to integers
    start = int(start_str)
    end = int(end_str)
    
    # Loop through the given range
    for j in range(start, end + 1):
        # Check condition divisible by 9 but not by 6
        if j % 9 == 0 and j % 6 != 0:
            # Add number to list
            num.append(j)

    # Display the result
    print(f"The number between {start} and {end} that are divisible by 9 but not by 6 are")
    print(num)

# If user enters invalid choice
else:
    print("Invalid choice")
    exit()