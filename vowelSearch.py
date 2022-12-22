def vowelSearch(word):
    bigWord = word.upper()
    
    wordList = []
    wordList[:0] = bigWord
    
    vowelList = ['A', 'E', 'I', 'O', 'U']
    
    vowelCount = 0
    vowels = []

    for vowel in vowelList:    
        if vowel in wordList:
            vowelCount += 1
            vowels.append(vowel)
    
    if len(vowels) > 1:
        print ('There are', vowelCount,'vowels in "'+ word.lower()+'", they are:', end =" ")
        print (vowels)
        if ('Y') in wordList:
            print ("\"Y\" is also in \"" +word.lower() +"\", but, is that really a vowel?")
        else:
            pass
    elif len(vowels) == 1:
        print('There is 1 vowel in "'+ word.lower() + '", it is: ', end="")
        print (vowels)
        if ('Y') in wordList:
            print ("\"Y\" is also in \"" +word.lower() +"\", but, is that really a vowel?")
        else:
            pass
    else:
        print('No vowels found in, "'+ word.lower()+ '"')
        if ('Y') in wordList:
            print ("Y is in \"" +word.lower() +"\", but is that really a vowel?")
        else:
            pass

vowelSearch('')
