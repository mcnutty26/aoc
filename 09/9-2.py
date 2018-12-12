from collections import deque
game = (411,7117000)
board = deque([0])
scores = []
player = 0
current = 0
for p in range(game[0]): scores.append(0)
for i in range(1,game[1]+1):
    if i % 23 != 0:
        board.rotate(-1)
        board.append(i)
    else:
        board.rotate(7)
        scores[player] += i +  board.pop()
        board.rotate(-1)
    player = (player + 1) % game[0]
print(max(scores))
