# 2445 별찍기 - 8 (Bronze 3)

def solution():
    a = int(input())
    for i in range(1, a+1):
        print('*'*i + ' '*((a*2)-(i*2)) + '*'*i)
    for i in range(1, a+1):
        print('*'*(a-i) + ' '*(i*2) + '*'*(a-i))
solution()