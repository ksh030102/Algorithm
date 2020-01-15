# 2577 숫자의 개수

import sys

def solution():
    result = [0]*10
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    SUM = a * b * c
    while SUM != 0:
        result[SUM%10]+=1
        SUM=SUM//10
    for i in result:
        print(i)
solution()
