#1546 평균 (Bronze 1)

sub = int(input())
score = list(map(int, input().split()))
s = 0
m = max(score)
for i in score:
    s += (i/m) * 100
print(s/sub)