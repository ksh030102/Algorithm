# 2441 별찍기 - 4 (Bronze 3)

def solution():
    a = int(input())
    for i in range(1,a+1):
        print(' '*(i-1) + '*'*(a+1-i))
solution()