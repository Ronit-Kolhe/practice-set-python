
questions = [
    ["Who is Charles Leclerc?", "Actor", "F1 Driver", "Chef", "Gangster", 1],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "Madrid", 1],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Mercury", 1],
    ["Who wrote 'Hamlet'?", "Mark Twain", "William Shakespeare", "Charles Dickens", "Leo Tolstoy", 1],
    ["What is H2O commonly known as?", "Salt", "Oxygen", "Water", "Hydrogen", 2],
    ["Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Rhino", 1],
    ["Who painted the Mona Lisa?", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Claude Monet", 1],
    ["What is the fastest land animal?", "Cheetah", "Horse", "Tiger", "Kangaroo", 0],
    ["Which programming language is known as the backbone of web development?", "Python", "C++", "JavaScript", "Rust", 2],
    ["What gas do plants absorb during photosynthesis?", "Carbon Dioxide", "Oxygen", "Nitrogen", "Helium", 0],
]
prize = 0
for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    ans = int(input("Enter your answer (1-4): ")) - 1  # shift to 0-based
    if question[5] == ans:
        print("Correct answer!\n")
        prize +=1000000
        print(f"you won: {prize}")
    else:
        print("Sorry brother, better luck next time.\n")
        break

print(f"your total winnigs are: {prize}")

if (prize >= 10000000):
    print("You've won the jackpot")
elif (prize >= 7500000):
    print("You've won the Excelent money")
elif (prize >= 5000000):
    print("You've won the Good money")
elif (prize >= 1000000):
    print("You've won the Average")
else:
    print("Sorry, You must try better next time")