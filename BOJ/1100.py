# 1100 하얀 칸
# 1번 풀이
# cnt = 0
# for i in range(8):
#     board = list(map(str, input()))
#     for j in range(len(board)):
#         if i % 2 == 0 and j % 2 == 0 and board[j] == 'F':
#             cnt += 1
#         elif i % 2 != 0 and j % 2 != 0 and board[j] == 'F':
#             cnt += 1
# print(cnt)

# 2번 풀이
#
# cnt = 0
# for i in range(8):
#     board = list(map(str, input()))
#     if i % 2 == 0:
#         for j in range(0, 8, 2):
#             if board[j] == 'F':
#                 cnt += 1
#     else:
#         for j in range(1, 7, 2):
#             if board[j] == 'F':
#                 cnt += 1
# print(cnt)

# 3번 풀이
cnt = 0
for i in range(8):
    board = list(map(str, input()))
    cnt += board[i%2::2].count('F')
    # if i % 2 == 0:
    #     cnt += board[0::2].count('F')
    # else:
    #     cnt += board[1::2].count('F')
print(cnt)