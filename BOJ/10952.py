# 10952 A+B - 5

import sys
def solution():
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a + b == 0:
            break
        print(a+b)
solution()
