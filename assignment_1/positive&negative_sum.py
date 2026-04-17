# Create two lists to store positive and negative numbers
num_pos_ve = []
num_neg_ve = []

# Start an infinite loop to repeatedly show menu
while True:
    
    # Display menu and take user choice
    a = int(input("""
Press 1 to enter number
Press 2 to calculate and print the sum
Press 3 to exit
Choice """))

    # If user chooses to enter a number
    if a == 1:
        
        # Take number input
        num = int(input("Enter the number "))
        
        # Check if number is positive or zero
        if num >= 0:
            # Store in positive list
            num_pos_ve.append(num)
        else:
            # Store in negative list
            num_neg_ve.append(num)

    # If user chooses to calculate sums
    elif a == 2:
        
        # Calculate sum of positive numbers
        total_pos = sum(num_pos_ve)
        
        # Calculate sum of negative numbers
        total_neg = sum(num_neg_ve)

        # Display positive numbers and their sum
        print("Positive numbers", num_pos_ve)
        print("Sum of positive numbers", total_pos)

        # Display negative numbers and their sum
        print("Negative numbers", num_neg_ve)
        print("Sum of negative numbers", total_neg)

    # If user chooses to exit the program
    elif a == 3:
        print("Exiting program")
        break

    # Handle invalid menu choice
    else:
        print("Invalid choice try again")