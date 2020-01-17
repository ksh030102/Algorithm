# 2442 별찍기 - 5 (Bronze 3)

def solution():
    a = int(input())
    for i in range(1,a+1):
        print(' '*(a-i)+'*'*(-1+(i+i)))
solution()