def getAvailableLetters(lettersGuessed):
    import string
    lowerletters = string.ascii_lowercase
    for L in lettersGuessed:
        for P in lowerletters:
            if P == L:  
                lowerletters = lowerletters.replace(L,'_')
    return(lowerletters)
    