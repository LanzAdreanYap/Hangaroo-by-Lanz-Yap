def isWordGuessed(secretWord, lettersGuessed):
    check=0
    for S in secretWord:
        for L in lettersGuessed:
            if L==S:
                check += 1
                break
            elif L!=S:
                pass
    return(check==len(secretWord))