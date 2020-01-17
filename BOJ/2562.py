# 2562 최댓값 (Bronze 2)
import sys
def solution():
    arr = []
    MAX = 0
    flag = 0
    for i in range(9):
        a = int(sys.stdin.readline())

        arr.append(a)
        if MAX < a:
            MAX = a
            flag = i

    print(MAX,flag+1)
solution()