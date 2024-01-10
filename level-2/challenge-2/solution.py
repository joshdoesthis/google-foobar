def solution(src, dest):
    if src == dest:
        return 0

    moves = [next_available_moves(src)]

    while dest not in moves[-1]:
        next_moves = []
        for square in moves[-1]:
            next_moves += next_available_moves(square)
        moves.append(next_moves)
    
    return len(moves)

def next_available_moves(square):
    board = [list(range(i, i + 8)) for i in range(0, 64, 8)]
    directions = [
        (1, -2),
        (-1, -2),
        (1, 2),
        (-1, 2),
        (2, -1),
        (2, 1),
        (-2, -1),
        (-2, 1),
    ]
    available_moves = []
    for move in directions:
        x = square % 8
        y = square // 8
        x += move[0]
        y += move[1]
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            available_moves.append(board[y][x])
    
    return available_moves