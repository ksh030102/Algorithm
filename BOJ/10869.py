# 10869 사칙연산

import sys

def solution():
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
solution()
