# 10817 세 수

import sys

def solution():
    a, b, c = map(int, sys.stdin.readline().split())
    arr = [a,b,c]
    arr.sort()
    print(arr[1])
solution()
