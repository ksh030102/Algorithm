# 2443 별찍기 - 7 (Bronze 3)

def solution():
    a = int(input())
    for i in range(1, a + 1):
        print(' ' * (a - i) + '*' * (-1 + (i + i)))
    for i in range(2, a + 1):
        print(' '*(i-1) + '*'*(a+a-i-i+1))
solution()