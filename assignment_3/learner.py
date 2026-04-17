"""
this program defines a learner class
it stores basic details of a learner
user inputs all required attributes
an object is created using those inputs
finally it displays the learner details
"""

class Learner:
    """
    class to represent a learner with basic information
    """

    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        """
        initialize learner attributes
        """
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def display_details(self):
        """
        display learner details in a formatted way
        """
        print("\nlearner details")
        print("-" * 30)
        print(f"roll no: {self.roll_no}")
        print(f"full name: {self.full_name}")
        print(f"address: {self.address}")
        print(f"enrollment year: {self.enrollment_year}")
        print(f"program: {self.program}")
        print(f"group: {self.group}")


# take input from user
roll_no = input("enter roll number: ")
full_name = input("enter full name: ")
address = input("enter address: ")
enrollment_year = input("enter enrollment year: ")
program = input("enter program: ")
group = input("enter group: ")

# create learner object
learner = Learner(roll_no, full_name, address, enrollment_year, program, group)

# display details
learner.display_details()