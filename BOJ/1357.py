# 1357 뒤집힌 덧셈
def Rev(n):
    i = list(str(n))
    print(i)
    j = sorted(i, reverse=True)
    return j

x, y = map(int, input().split())

print(Rev(x), Rev(y))