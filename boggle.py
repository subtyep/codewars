def find_word(board, word):
    # list to keep track of what letters we have used in our search
    usedLetters = []

    def is_out_of_bounds(spot):
        if spot[0] < 0 or spot[0] >= len(board):
            return True
        elif spot[1] < 0 or spot[1] >= len(board):
            return True
        else:
            return False

    def is_adjacent(one, two):
        if is_out_of_bounds(one) or is_out_of_bounds(two):
            return False

        if one[0] == two[0] and one[1] == two[1]:
            return False

        return abs(one[0] - two[0]) in [0, 1] and abs(one[1] - two[1]) in [0, 1]

    def get_adjacent(l):
        return [spot for spot in letters if is_adjacent(l, spot) and spot not in usedLetters]

    # begin the recursive fun!
    def get_next_letter(letter, depth):
        adjacentLetters = [adj for adj in get_adjacent(letter) if word[depth] == adj[2]]

        #stop recursing if we are on the last letter, and we found adjacent matches
        if depth == len(word) - 1 and len(adjacentLetters) > 0:
            # we did it!
            usedLetters.append(adjacentLetters[0])
            return True

        if (len(adjacentLetters) == 0):
            return False

        for adjacentLetter in adjacentLetters:
            usedLetters.append(adjacentLetter)
            if get_next_letter(adjacentLetter, depth + 1):
                # we did it!
                return True
            else:
                usedLetters.pop()

    # collapse the board to a single list
    letters = []
    for rowNum in range(len(board)):
        for colNum in range(len(board)):
            # tuple with rowCoordinate, columnCoordinate, letter
            letters.append((rowNum, colNum, board[rowNum][colNum]))

    # get all the spots with the first letter of the word
    startingLetters = [starts for starts in letters if starts[2] == word[0]]

    # check for the simple case that the word is one letter long
    if len(word) == 1 and len(startingLetters) > 0:
        return True

    for startingLetter in startingLetters:
        # mark this letter as used
        usedLetters.append(startingLetter)
        if get_next_letter(startingLetter, 1):
            # we did it!
            return True
        else:
            # this letter did't work out
            usedLetters = []

    # welp, didn't find anything
    return False


#testing, not part of solution
theBoard = \
    [
        ["E", "A", "R", "A"],
        ["N", "L", "E", "C"],
        ["I", "A", "I", "S"],
        ["B", "Y", "O", "R"]
    ]

print(find_word(theBoard, "C"))#, True, "Test for C")
print(find_word(theBoard, "EAR"))#, True, "Test for EAR")
print(find_word(theBoard, "EARS"))#, False, "Test for EARS")
print(find_word(theBoard, "BAILER"))#, True, "Test for BAILER")
print(find_word(theBoard, "RSCAREIOYBAILNEA"))#, True, "Test for RSCAREIOYBAILNEA")
print(find_word(theBoard, "CEREAL"))#, False, "Test for CEREAL")
print(find_word(theBoard, "ROBES"))#, False, "Test for ROBES")