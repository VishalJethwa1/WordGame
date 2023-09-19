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
            print("CRACK A WORD")
            print("Select Level | 1 for Beginner | 2 for Moderate | 3 for Advance")

            selectMode = int(input("Level")) #user will pass level here

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
            elif selectMode > 3 or selectMode < 1:
                continue
            else:
                randomWord = None
        except:
            print("Please select level by pressing numbers : 1 | 2 | 3")
            continue
        
        j = 0
        while j < maxAttempts: 
            print(f"Level : {selectMode} \t Attempts : {maxAttempts}")
            userGuessedWord = input(f"Guess a {len(randomWord)} letter word\n\t")
            if userGuessedWord == "":
                print("Blank Guess! \nType n Hit Enter")
                maxAttempts += 1
            elif userGuessedWord != "" and len(userGuessedWord) > len(randomWord) and len(userGuessedWord) < len(randomWord):
                beginner.append(userGuessedWord)
            maxAttempts -= 1
            getWordFromList = randomWord
            #print(getWordFromList) #print for test purpose
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
            #revealedWord = revealedWord.upper()
            print("\t"+revealedWord) # this will show players guess, if guess matched, word will be revealed otherwise unmatched letters in word will be shown dash instead 
            if revealedWord == userGuessedWord:
                revealedWord = revealedWord.upper()
                print("Congratulations! You cracked a word")
                print(f"Word : {revealedWord} \t Attempts : {maxAttempts}")
                break
            elif revealedWord != userGuessedWord and maxAttempts == 0:
                getWordFromList = getWordFromList.upper()
                print(f"\t\tYOU LOSE! \n\tWORD: {getWordFromList} \tATTEMPTS : {maxAttempts}  \n\t\tTry Again")
                print("------------------------------------")
                continue
        j+=i
          
        if maxAttempts > 0:
            break
    
    
    i+=1
    
main()
