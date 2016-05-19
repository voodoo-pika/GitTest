def checkio(words):
    newwords=words.split()
    x=len(newwords)
    result=0
    for word in newwords:
        if word.isalpha() and x>2:
            result+=1
            if result==3:
                print ("t")
                return True
        else:
            print ("f", x)
            return False
checkio("He")