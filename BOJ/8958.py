# 8958 OX퀴즈

n = int(input())
cnt = 0
s = 0
for i in range(n):
    cnt = 0
    s = 0
    for j in input():
        if j == 'O':
            cnt += 1
            s += cnt
        else:
            cnt = 0
    print(s)