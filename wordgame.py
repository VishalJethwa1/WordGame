import random

beginner = ["able", "blow", "cake", "dine", "east", "fish", "game", "hell", "iron", "jack"]
moderate = ["attack", "behave", "camera", "dealer", "easter", "feeling", "glacier", "hunger", "jailer"]
advance = ["abstract", "believe", "cupboard", "director", "egoistic", "failure", "greetings", "fighter"]

  
def main():
    global randomWord
    global maxAttempts
    i = 1
    while i > 0: #this loop will continuously display select mode screen
        print("Press 1 for Beginner Mode")
        print("Press 2 for Moderate Mode")
        print("Press 3 for Advance Mode")

        selectMode = int(input("Select Mode"))

        randomWord = None
        maxAttempts = None

        if selectMode == 1:
            randomWord = random.choice(beginner)
            maxAttempts = 3
        elif selectMode == 2:
            randomWord = random.choice(moderate)
            maxAttempts = 4
        elif selectMode == 3:
            randomWord = random.choice(advance)
            maxAttempts = 6
        else:
            randomWord = None
        
        j = 0
        while j < maxAttempts:
            userGuessedWord = input("Guess your word")
            getWordFromList = randomWord
            revealedWord = ""
            i = 0
            length = len(userGuessedWord)
            while i < length:
                if userGuessedWord[i] == getWordFromList[i]:
                    revealedWord += userGuessedWord[i]
                else:
                    revealedWord += "_ "
                i+= 1

            print(revealedWord)
            maxAttempts -= 1
        j+=i

    i+=1

main()

# userInput = input("Guess your word")
# print(userInput)

# wordFromList = ["truth", "knowledge", "bliss"]
# getRandomWord = random.choice(wordFromList)
# guessedWord = ""
# i = 0
# length = len(userInput)
# while i < length:
#     if userInput[i] == getRandomWord[i]:
#         guessedWord += userInput[i]
#     else:
#         guessedWord += "_ "
#     i+= 1

# print(guessedWord)