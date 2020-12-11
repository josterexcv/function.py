def countWordsFromFile():
    fileName = input("Enter the file name:- ")

    numberOfWords = 0

    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        number OfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()        