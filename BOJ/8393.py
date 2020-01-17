# 8393 합 (Bronze 5)

def solution():
    a = int(input())
    # sum = 0
    # for i in range(1,a+1):
    #     sum = sum + i
    if a%2==0:
        Sum = (1+a) * (a//2)
    else:
        Sum = (1+a) * (a//2) + (1+a)//2
    print(Sum)
solution()