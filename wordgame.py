import random

beginner = ["able", "blow", "cake", "dine", "east", "fish", "game", "hell", "iron", "jack"]
moderate = ["attack", "behave", "camera", "dealer", "easter", "feeling", "glacier", "hunger", "jailer"]
advance = ["abstract", "believe", "cupboard", "director", "egoistic", "failure", "greetings", "fighter"]
  
def main():
    global randomWord
    global maxAttempts
    i = 1
    while i > 0: #this loop will continuously display select mode screen
        try:
            print("Select Level | 1 for Beginner | 2 for Moderate | 3 for Advance")

            selectMode = int(input("Select Level"))

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
        except:
            print("Please select level by pressing numbers : 1 | 2 | 3")
            continue
        
        j = 0
        while j < maxAttempts:
            print("CRACK A WORD")
            print(f"Level : {selectMode} \t Attempts : {maxAttempts}")
            userGuessedWord = input("Guess your word\n")
            maxAttempts -= 1
            getWordFromList = randomWord
            print(getWordFromList)
            revealedWord = ""
            i = 0
            length = len(getWordFromList)
            try:
                while i < length:
                    if userGuessedWord[i] == getWordFromList[i]:
                        revealedWord += userGuessedWord[i]
                    else:
                        revealedWord += " _ "
                    i+= 1
            except:
                 continue    
            print(revealedWord) #test statement
            if revealedWord == userGuessedWord:
                print("Congratulations! You cracked a word")
                break
            else:
                print("")
              
        j+=i
          
        if maxAttempts > 0:
            break
    
    
    i+=1
    
main()
