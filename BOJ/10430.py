# 10430 나머지

import sys
def solution():
    a, b, c = map(int, sys.stdin.readline().split())
    print((a+b)%c)
    print(((a+b)%c)%c)
    print((a*b)%c)
    print(((a*b)%c)%c)
solution()
