def is_armstrong(num_str):
    # Convert string to integer
    if not num_str.isdigit():
        return "invalid input enter a numeric string."

    num = int(num_str)
    power = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** power

    if total == num:
        return f"{num} is an armstrong number."
    else:
        return f"{num} is not an armstrong number."


# Example usage
user_input = input("Enter a number: ")
result = is_armstrong(user_input)
print(result)