# 2884 알람시계

import sys

def solution():
    h, m = map(int, sys.stdin.readline().split())
    if m >= 45:
        m -= 45
    else:
        if h == 0:
            h = 23
        else:
            h = h - 1
        m = 60 - 45 + m
    print(h, m)
solution()
