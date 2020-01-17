# 2443 별찍기 - 6 (Bronze 3)

def solution():
    a = int(input())
    for i in range(1, a + 1):
        #print(' ' * (a - i) + '*' * (-1 + (i + i)))
        print(' '*(i-1) + '*'*(a+a-i-i+1))
solution()