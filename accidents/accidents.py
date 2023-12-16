import csv

# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9

def main():
    # Prompt the user for a filename and open that text file.
    filename = input("Name of file that contains NHTSA data: ")

    try:
        with open(filename, "rt") as text_file:
            # Prompt the user for a percentage.
            perc_reduc = float(input("Percent reduction of texting while driving [0, 100]: "))
            
            if not 0 <= perc_reduc <= 100:
                print("Percentage must be between 0 and 100.")
            else:
                print()
                print(f"With a {perc_reduc}% reduction in using a cell",
                    "phone while driving, approximately the",
                    "following number of injuries and deaths",
                    "would have been prevented in the USA.", sep="\n")
                print()
                print("Year, Injuries, Deaths")

                # Use the csv module to create a reader
                # object that will read from the opened file.
                reader = csv.reader(text_file)

                # The first line of the CSV file contains column headings
                # and not a student's I-Number and name, so this statement
                # skips the first line of the CSV file.
                next(reader)

                # Process each row in the CSV file.
                for row in reader:
                    year = row[YEAR_COLUMN]

                    # Call the estimate_reduction function.
                    injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)

                    # Print the estimated reductions
                    # in injuries and fatalities.
                    print(year, injur, fatal, sep=", ")

    except ValueError as val_err:
        print(val_err, f"\nYou typed an invalid floating point number or it's out of range, please try again.")
            
    except FileNotFoundError as not_found_err:
        print(not_found_err, "\nYou typed a name of a file that doesn't exist. Please try retyping the name of the file again.")

    except ZeroDivisionError as zer_div:
        print(zer_div, f"The file {filename} contains a 0 in row {row} in the behavior or fatal_crashes index and the program tried to divide by 0 wich is not possible.\nPlease fix the 0 and try again")

    except csv.Error as csv_err:
        print(f"The file {filename} cointains a csv error in row {row}, remember that csv means comma separated values, so it should only contain values and commas. \nPlease try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that
    would not have occurred on U.S. roads and highways if drivers
    had reduced a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal

# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
