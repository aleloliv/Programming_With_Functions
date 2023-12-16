import random

def main():
    numbers = [16.2, 75.1, 52.3] # Crates and initiate a list of floating points numbers
    print(f"Numbers = {numbers}")
    
    append_random_numbers(numbers) # Calls the append_random_numbers function and appends 1 random number to the list from -1000 to 1000
    
    print(f"Numbers = {numbers}")
    
    append_random_numbers(numbers, 3) # Calls the append_random_numbers 3 times
    
    print(f"Numbers = {numbers}")
    
    words = ["serendipity", "quixotic", "effervescent"] # Creates and initiates a list of words
    
    print(f"Words = {words}")

    float_number = random.uniform(1, 100) # Picks a random number from 1 to 100
    int_number = int(round(float_number)) # Rounds and transforms the floating point number into an integer
    
    append_random_words(words, int_number)  # Calls the append_random_words a random number of times
    
    print(f"Words = {words}")

    #---------------------------------------------------------------------------------------------------------
    print("\n\nNow it's your turn to control the functions!\n")

    user_numbers = []
    number_of_numbers = int(input("Please insert an integer: "))

    user_append_random_numbers(user_numbers, number_of_numbers) # Calls the user_append_random_numbers that appends numbers that the user chooses to the user's list

    print(f"Your numbers = {user_numbers}")

def append_random_numbers(numbers_list, quantity=1): # Appends a random number to a list x times (1 by default)
    for x in range(quantity):
        num = random.uniform(-1000, 1000) # Generates a random number from -1000 to 1000
        num = round(num, 1)
        numbers_list.append(num)

def append_random_words(words_list, quantity=1): # Appends a random word from a static list to a list of words x times (1 by default)
    random_words = [
    "apple", "banana", "chocolate", "dolphin", "elephant", "flamingo", "giraffe", "hamburger", "ice cream", "jacket",
    "koala", "lemon", "mango", "narwhal", "octopus", "penguin", "quokka", "rhinoceros", "strawberry", "tiger",
    "umbrella", "violin", "watermelon", "xylophone", "yogurt", "zebra", "avocado", "broccoli", "carrot", "dragon",
    "eagle", "fox", "gazelle", "hedgehog", "iguana", "jackal", "kiwi", "lemur", "meerkat", "newt",
    "opossum", "parrot", "quail", "raccoon", "seahorse", "toucan", "iguana", "lynx", "marmoset", "nutria",
    "otter", "puma", "quokka", "reindeer", "sloth", "tapir", "urutu", "vulture", "weasel", "x-ray tetra",
    "yeti", "zebu", "agave", "bison", "cactus", "daisy", "eucalyptus", "fig", "geranium", "hibiscus",
    "iris", "jasmine", "kiwifruit", "lily", "magnolia", "narcissus", "orchid", "pansy", "quince", "rose",
    "sunflower", "tulip", "violet", "wisteria", "xerophyte", "yarrow", "zinnia", "alpaca", "butterfly", "chameleon",
    "dalmatian", "elephant seal", "fennec fox", "giraffe", "himalayan cat", "iguana", "jellyfish", "kangaroo", "lemur", "manatee"] 
    # The list contains 100 random words

    for x in range(quantity):
    	words_list.append(random.choice(random_words))

def user_append_random_numbers(user_numbers_list, quantity = 1):
    n = quantity
    for x in range(quantity):
        number = float(input(f"Insert a number ({n}/{quantity}): "))
        user_numbers_list.append(number)
        n -= 1

if __name__ == "__main__":
    main()