questions = ("What is the speed of light", "What is this coded in", "TetoTetoTetoTeto")
options = (("299792458 m/s", "300000000 m/s", "1 km/h", "0401"), ("Java", "C++", "Python", "Lua"), ("Teto", "Teto", "Teto", "Teto"))
answers = ("299792458 m/s", "Python", "Teto")

running = True
while running:
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        for j in range(len(options[i])):
            print(f"{chr(j + 65)}: {options[i][j]}")
        answer = input("")
        if (options[i][ord(answer) - 65] == answers[i]):
            score += 1
            print("Correct")
        else:
            print("Incorrect")
    print(f"Final Score: {score}/{len(questions)}")
    if (input("Retry? (y/n)\n") == "n"):
        running = False