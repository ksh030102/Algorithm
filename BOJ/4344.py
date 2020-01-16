# 4344 평균은 넘겠지

import sys

def solution():
    
    std = int(input())
    cnt=[0]*std
    j=0
    for i in range(std):
        score = list(map(int, sys.stdin.readline().split()))
        SUM = sum(score)-score[0]
        avg = SUM/score[0]
        for i in range(1,score[0]+1,1):
            if score[i]>avg:
                cnt[j]+=1
        cnt[j] = (cnt[j]/score[0]) *100
        round(cnt[j],3)
        j+=1

    for i in cnt:
        print('%.3f'%i + '%')
solution()
        
