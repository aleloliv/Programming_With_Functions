import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    pupils = read_compound_list("pupils.csv") # calls the read_coumpound_list function and gives the pupils csv file as paramether to open it and extract its information into a compound list

    extract_month_and_day = lambda birthdate: birthdate[5:] # creates a lambda function that extracts the month and day from a date in format YYYY-MM-DD

    birthdate_func = lambda pupil: extract_month_and_day(pupil[BIRTHDATE_INDEX]) # creates a lambda function that extracts the birthdate from the compound list pupils

    sorted_list = sorted(pupils, key=birthdate_func) # sorts the compound list pupils by birthdate

    # given_name_func = lambda pupils: pupils[GIVEN_NAME_INDEX] # creates a lambda function that extracts the given name from the compound list pupils

    # sorted_list = sorted(pupils, key=given_name_func) # sorts the compound list pupils by given name

    print_list(sorted_list) # calls the function print_list that will print the sorted list
    

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):
    for element in list:
        print(element)

if __name__ == "__main__":
    main()