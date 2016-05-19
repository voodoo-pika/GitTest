def checkio(words):
    spl=words.split()
    sam = 0
    if len(spl)>2:
        for word in spl:
            if word.isalpha():
                sam+=1
                if sam == 3:
                    print ("true")
            else:
                sam = 0
                print ("false")
    else:
        print ("false")
checkio("hi hi 123 hi")