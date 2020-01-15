# 10818 최소, 최대

import sys

def solution():
    l = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    print(a[0], a[l-1])
solution()
