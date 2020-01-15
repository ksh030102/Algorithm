# 10886 0 = not cute / 1 = cute

import sys

def solution():
    a = int(input())
    vote = 0
    for i in range(a):
        b = int(input())
        if b == 1:
            vote+=1
        else:
            vote-=1
    if vote < 0:
        print("Junhee is not cute!")
    else:
        print("Junhee is cute!")
solution()
