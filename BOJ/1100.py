# 1100 하얀 칸
cnt = 0
for i in range(8):
    board = list(map(str, input()))
    for j in range(len(board)):
        if (i % 2 == 0 and j % 2 == 0) and board[j] == 'F':
            cnt += 1
        elif i % 2 != 0 and j % 2 != 0 and board[j] == 'F':
            cnt += 1
        else:
            continue
print(cnt)