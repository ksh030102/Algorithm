# 11720 숫자의 합 (Bronze 2)

import sys
a = int(input())
num = list(input())
s = 0
for i in num:
    s += int(i)
print(s)