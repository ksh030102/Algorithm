# 11022 A+B - 8 (Bronze 3)

import sys
def solution():
    a = int(input())
    for i in range(a):
        c, b=map(int, sys.stdin.readline().split())
        print('Case #{}: {} + {} = {}'.format(i+1, c, b, c+b))
solution()