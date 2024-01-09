def solution(src, dest):
    # the distance from the knight to itself is 0
    # the distance from the knight to its next move can be one of +6, +10, +15, +17, -6, -10, -15, -17 squares
    # calculate the distance from the knight to the edge of the board
    knight_row = src // 8
    knight_col = src % 8

    relative_moves = [
        # check that a move is not off the board or on the same row as the knight
        6 if knight_col > 5 and 
    ]
    print(relative_moves)
    # the board is a 8x8 grid
    # the knight can only move to squares on the board
    # the knight can only move to squares it has not been to
    previous_moves = [src] # keep track of all the squares the knight has been to
    print(previous_moves)

print(solution(1, 1)) # 3