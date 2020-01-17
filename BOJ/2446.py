# 2446 별찍기 - 9 (Bronze 3)

def solution():
    a = int(input())
    for i in range(1,a):
        print(' ' * (i - 1) + '*' * (a + a - i - i + 1))
    for i in range(1,a+1):
        print(' '*(a-i) + '*'*(-1+i+i))
solution()