def countWordsFromFile():
    fileName = input("Enter file name: ")
    file = open(fileName, "r")
    noOfWords = 0

    for i in file:
        words = i.split()
        noOfWords = noOfWords+len(words)

    print(noOfWords)

countWordsFromFile()


