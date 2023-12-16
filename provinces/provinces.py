def main():
    text_list = read_list("provinces.txt") # Read the contents of provinces.txt into a list

    print(text_list) # Prints the entire list

    modified_list = modify_list(text_list) # Removes the first element from the list, removes the last element from the list, Replaces every AB in the list with ALberta
    print(modified_list) # Prints the new list

    value = count_alberta(modified_list) # Counts the number of times that the word Alberta shows up in the list
    print(f"Alberta occurs {value} times in the modified list")


def read_list(filename):
    text_list = [] # Initializes an empty list that will store the content of the file in it

    with open(filename, "rt") as text_file: # Opens the text file for reading and references the file in a variable named text_file
        for line in text_file: # Reads the contents of the file one line at a time
            clean_line = line.strip() # Cleans white spaces in the beggining and end of the line

            text_list.append(clean_line) # Appends each line to the list as a separate element

    return text_list

def modify_list(text_list):
    text_list.pop(0)
    text_list.pop(-1)

    for i in range(len(text_list)):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"

    return text_list
    
def count_alberta(text_list):
    count = text_list.count("Alberta")

    return count

# Call main to start this program
if __name__ == "__main__":
    main()