# 2588 곱셈

import sys

def solution():
    #a, b = map(int, sys.stdin.readlines().split())
    a = int(input())
    b = int(input())
    result = a*b
    while b>0:
        print(a*(b%10))
        b=b//10
    print(result)
solution()
