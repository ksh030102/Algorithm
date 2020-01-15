# 2822 점수계산

import sys

def solution():
    score = []
    for i in range(8):
        a = int(sys.stdin.readline())
        score.append(a)
    scores = score.copy()
    scores.sort()
    print(sum(scores[3:]))
    scores[0:3] = []
    for i in range(8):
        for j in scores:
            if score[i] == j:
                print(i+1)
                break
solution()
