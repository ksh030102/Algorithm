# 10039 평균 점수 단계별(실습1)
s = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    s = s + a
print(s//5)