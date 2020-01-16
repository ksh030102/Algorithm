# 10872 팩토리얼

import sys

def solution():
    n = int(sys.stdin.readline())
    if n == 0:
        print('1')
    else:
        print(fact(n))
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
solution()
