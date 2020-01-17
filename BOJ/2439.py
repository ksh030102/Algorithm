# 2439 별찍기 - 2

import sys
def solution():
    a = int(input())
    for i in range(1,a+1):
        print(' '*(a-i)+'*'*i)
solution()