game = (411,71170)
board = [0]
scores = []
player = 0
current = 0
for p in range(game[0]): scores.append(0)
for i in range(1,game[1]+1):
    if i % 23 != 0:
        position = current + 2
        while position > len(board): position -= len(board)
        board.insert(position,i)
        current = board.index(i)
    else:
        current -= 7
        while current < 0: current += len(board)
        scores[player] += i + board[current]
        board.remove(board[current])
    player = (player + 1) % game[0]
print(max(scores))
