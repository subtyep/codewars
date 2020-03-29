def boggle(board, word):
    # first do a sanity check to determine all the letters exist in the board, in the right quantity
    allLetters = [letter for row in board for letter in row]
    for letter in word:
        if letter in allLetters:
            allLetters.remove(letter)
        else:
            return False

    letters = []
    for rowNum in range(len(board)):
        for colNum in range(len(board)):
            #tuple with rowCoordinate, columnCoordinate, letter
            letters.append((rowNum, colNum, board[rowNum][colNum]))

    usedLetters = []

    def isOutOfBounds (spot):
        if spot[0] < 0 or spot[0] >= len(board):
            return True
        elif spot[1] < 0 or spot[1] >= len(board):
            return True
        else:
            return False

    def isAdjacent (one, two):
        #check out of bounds
        if isOutOfBounds(one) or isOutOfBounds(two):
            return False

        if one[0] == two[0] and one[1] == two[1]:
            return False

        return abs(one[0] - two[0]) in [0, 1] and abs(one[1] - two[1]) in [0, 1]


    def getAdjacent (l):
        return [spot for spot in letters if isAdjacent(l, spot)]

    #get all the spots with the first letter of the word
    startingLetters = [starts for starts in letters if starts[2] == word[0]]

    #begin the recursive fun!
    def recurseOnLetter(letter, depth):
        adjacentLetters = [adj for adj in getAdjacent(letter) if word[depth] == adj[2]]
        print('depth', depth, letters, adjacentLetters)
        if (len(adjacentLetters) == 0):
            return False

        for adjacentLetter in adjacentLetters:
            recurseOnLetter(adjacentLetter, depth + 1)

    for startingLetter in startingLetters:
        #mark this letter as used
        usedLetters.append(startingLetter)
        if recurseOnLetter(startingLetter, 1):
            #we did it!
            return True
        else:
            #this letter did't work out
            usedLetters = []






theBoard = \
    [["I", "L", "A", "W"],
     ["B", "N", "G", "E"],
     ["I", "U", "A", "O"],
     ["A", "S", "R", "L"]]
boggle(theBoard, 'BINGO')