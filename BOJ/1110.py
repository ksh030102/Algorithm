# 1110 더하기 사이클

import sys
def solution():
    n = int(input())
    N = n
    nn = n
    cnt = 0
    n = n%10 + (n//10)
    cnt+=1
    while n!=N:
        tmp = n
        n = n%10 + (nn%10)
        nn = tmp
        cnt+=1
    print(cnt)
solution()
