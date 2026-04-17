# Take input for subject names from the user
a = input("Enter the name of your first subject ")
b = input("Enter the name of your second subject ")
c = input("Enter the name of your third subject ")
d = input("Enter the name of your fourth subject ")
e = input("Enter the name of your fifth subject ")
f = input("Enter the name of your sixth subject ")

# Take input for marks of each subject
sub1 = int(input(f"Enter the marks in {a} "))
sub2 = int(input(f"Enter the marks in {b} "))
sub3 = int(input(f"Enter the marks in {c} "))
sub4 = int(input(f"Enter the marks in {d} "))
sub5 = int(input(f"Enter the marks in {e} "))
sub6 = int(input(f"Enter the marks in {f} "))

# Calculate total percentage
# Total marks assumed to be 600 since 6 subjects each out of 100
total_percentage = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 600 * 100

# Check percentage and assign division using if elif else
if total_percentage >= 85:
    # Distinction category
    print(f"{total_percentage} | Congratulations you got Distinction")
    
elif total_percentage >= 70 and total_percentage < 85:
    # First division category
    print(f"{total_percentage} | Congratulations you got First Division")
    
elif total_percentage >= 55 and total_percentage < 70:
    # Second division category
    print(f"{total_percentage} | Congratulations you got Second Division")
    
elif total_percentage >= 45 and total_percentage < 55:
    # Third division category
    print(f"{total_percentage} | You got Third Division")
    
else:
    # Fail condition
    print(f"{total_percentage} | sorry you are fail")