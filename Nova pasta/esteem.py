def explanation():
    print("This program is an implementation of the Rosenberg" +
        "Self-Esteem Scale. This program will show you ten" +
        "statements that you could possibly apply to yourself." +
        "Please rate how much you agree with each of the" +
        "statements by responding with one of these four letters:" +
        "\n"+
        "D means you strongly disagree with the statement." +
        "d means you disagree with the statement." +
        "a means you agree with the statement." +
        "A means you strongly agree with the statement.")
    

def questions(previous):
    if(previous == 0):
        question = "1. I feel that I am a person of worth, at least on an equal plane with others."
    elif(previous == 1):
        question = "2. I feel that I have a number of good qualities."
    elif(previous == 2):
        question = "3. All in all, I am inclined to feel that I am a failure."
    elif(previous == 3):
        question = "4. I am able to do things as well as most other people."
    elif(previous == 4):
        question = "5. I feel I do not have much to be proud of."
    elif(previous == 5):
        question = "6. I take a positive attitude toward myself."
    elif(previous == 6):
        question = "7. On the whole, I am satisfied with myself."
    elif(previous == 7):
        question = "8. I wish I could have more respect for myself."
    elif(previous == 8):
        question = "9. I certainly feel useless at times."
    elif(previous == 9):
        question = "10. At times I think I am no good at all."
    
    return question

def entry(answer):
    if (answer != "D" and answer != "d" and answer != "a" and answer != "A"):
        answer = input("Enter D, d, a, or A: ")

    return answer

def score(entry, question):
    if (question == 1 or question == 2 or question == 4 or question == 6 or question == 7):
        if (entry == "D"):
            points = 0
        elif (entry == "d"):
            points = 1
        elif (entry == "a"):
            points = 2
        elif (entry == "A"):
            points = 3
    elif (question == 3 or question == 5 or question ==8 or question == 9 or question == 10):
        if (entry == "D"):
            points = 3
        elif (entry == "d"):
            points = 2
        elif (entry == "a"):
            points = 1
        elif (entry == "A"):
            points = 0

    return points

def main():
    explanation()

    previous = 0
    points = 0   
    for x in range(10):
        question = questions(previous)
        print(f"{question}")
        answer = input("Enter D, d, a, or A: ")
        choice = entry(answer)
        numbers = score(choice, previous + 1)
        points += numbers
        previous += 1

    print(f"Your score is {points}.\nA score below 15 may indicate problematic low self-esteem.")

main()