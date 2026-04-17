"""This program takes student details from the user and saves them into a CSV file as a new record."""


import csv

def add_record():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")
    prg = input("Enter prgram: ")
    year = input("Enter Year: ")
    grp = input("Enter Group: ")

    records_field = ['student_name', 'roll_no', 'program', 'year', 'group']

    with open('records.csv','a', newline='') as csvfile:  
        writer = csv.DictWriter(csvfile, fieldnames=records_field)    
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'student_name': name, 'roll_no': roll, 
            'program': prg, 'year': year, 'group': grp
        })        
    print("Record added successfully.")

if __name__ == "__main__":
    add_record()


    