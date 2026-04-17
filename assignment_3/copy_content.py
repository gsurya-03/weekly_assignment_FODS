"""
this program copies content from one file to another
user enters input file name and output file name
it uses try except to handle errors
it shows error if input file does not exist
it also shows error if output file already exists
"""

# take file names from user
input_file = input("enter input file name: ")
output_file = input("enter output file name: ")

try:
    # try opening input file in read mode
    with open(input_file, "r") as f:
        data = f.read()

    # check if output file already exists
    try:
        with open(output_file, "x") as f:
            # write data into new file
            f.write(data)
        print("file copied successfully")

    except FileExistsError:
        print("output file already exists")

except FileNotFoundError:
    print("input file does not exist")