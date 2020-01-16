# 10871 X보다 작은 수

import sys

def solution():
    N, X = map(int, sys.stdin.readline().split())
    n = list(map(int, sys.stdin.readline().split()))
    for i in n:
        if i < X:
            print(i)
solution()
