def getGuessedWord(secretWord,lettersGuessed):
    for S in secretWord:
        if S == '_' or S == ' ':
            continue
        elif (S in lettersGuessed) == False:
            secretWord = secretWord.replace(S,'_ ')
    return(secretWord)