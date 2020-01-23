# 1110 더하기 사이클

import sys
def solution():
    a = int(input())
    num = a
    cnt = 0
    chk_num = '0'
    new_num = a//10+a%10
    a = a%10 + new_num%10
    while chk_num != str(num):
        new_num = new_num%10 + a%10
        cnt += 1
        chk_num = str(a%10) + str(new_num%10)
        a = int(chk_num)
    print(cnt)
solution()
