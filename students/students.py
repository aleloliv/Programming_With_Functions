import csv
import re  # Import the regular expression module

def read_dictionary(filename):
    students = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[0]
                students[key] = row_list
    return students

def main():
    students = read_dictionary("students.csv")
    number = input("Insert a student I-Number: ")

    number = number.replace("-", "")

    if len(number) > 9:
        print("Invalid I-Number: too many digits")
    elif not number.isdigit():
        print("Invalid I-Number")
    else:
        if number in students:
            student = students[number]
            print(student)
        else:
            print("No such student")
    
if __name__ == "__main__":
    main()