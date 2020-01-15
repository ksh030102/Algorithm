# 1085 직사각형에서 탈출

import sys

def solution():
    hans = list(map(int,sys.stdin.readline().split()))
    a = [hans[0],hans[1],hans[2]-hans[0],hans[3]-hans[1]]
    print(min(a))
solution()
