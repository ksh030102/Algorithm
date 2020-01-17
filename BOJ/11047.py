# 11047 동전 0 (Silver 1)

import sys
def solution():
    a, money = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(a):
        c = int(input())
        arr.append(c)
    # for i in range(a):
    #     if arr[i] > b:
    #         break
    cnt = 0
    while money != 0 and i >= 0:
        if arr[i] <= money:
            cnt += money//arr[i]
            money = money % arr[i]
        i-=1
    print(cnt)
solution()