def chooseWord():
    import random 
    loadWords = ["apple","banana","engineering","programming","calculus","physics","glass","refrigerator"]
    return(random.choice(loadWords))
    
def Hangaroo():
    import string
    
    secretWord = chooseWord()
    
    lettersGuessed=[]
    list(lettersGuessed)
    mistakesMade = 0
    lword = len(secretWord)
    
    print("HANGAROO: GUESS THE SECRET WORD")
    print("You have unlimited guesses but your mistakes are counted")
    print("Number of Mistakes: ", mistakesMade)
    print("")
    print("Start Guessing the Word with",lword,"Letters!")
    print(getGuessedWord(secretWord,lettersGuessed))
    
    while isWordGuessed(secretWord,lettersGuessed) == False:
        guess = input("Guess a Letter: ")
        guessedL = guess.lower()
        
        if len(guessedL)!=1 or (guessedL in string.ascii_lowercase) == False:
            print("")
            print("You have an Invalid Input! Try Again")
            print("")
        elif (guessedL in secretWord) == False and (guessedL in lettersGuessed) == False:
           mistakesMade += 1
           print("")
           print("Wrong guess!")
           print("Mistakes: ",mistakesMade)
           print("")
           lettersGuessed.append(guessedL)
        elif (guessedL in lettersGuessed) == True:
            print("")
            print("You've already guessed that. Try again!")
        else:
            print("")
            print("Way to Go! You've guessed that right.")
            print("")
            lettersGuessed.append(guessedL)
      
        print("Letters Available: ", getAvailableLetters(lettersGuessed))
        print("")
        print(getGuessedWord(secretWord,lettersGuessed))
 
    if isWordGuessed(secretWord,lettersGuessed) == True: 
        print("")
        return(print("You've Finally Guessed The Word:",secretWord))
    
    