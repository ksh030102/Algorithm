# 10950 A+B - 3

import sys

def solution():
    c = int(input())
    for i in range(c):
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
solution()
