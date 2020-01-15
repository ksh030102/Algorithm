# 2490 윷놀이

import sys

def solution():
    for i in range(3):
        a = list(map(int, sys.stdin.readline().split()))
        b = sum(a)
        if b == 3:
            print('A')
        elif b == 2:
            print('B')
        elif b == 1:
            print('C')
        elif b == 0:
            print('D')
        else:
            print('E')
solution()
