# 1330 두수비교하기

import sys

def solution():
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')
solution()
