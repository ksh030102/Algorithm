# 2920 음계 (Bronze 2)
import sys

def solution():
    music = list(map(int, sys.stdin.readline().split()))
    # m = [1, 2, 3, 4, 5, 6, 7, 8]
    # dis = sorted(m, reverse=True)
    if music == sorted(music):
        print('ascending')
    elif music == sorted(music, reverse=True):
        print('descending')
    else:
        print('mixed')
solution()