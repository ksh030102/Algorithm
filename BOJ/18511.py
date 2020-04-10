# 18511 큰 수 구성하기

n, s = map(int, input().split())
k = list(map(int, input().split()))
nn = list(str(n))
a = []
for i in range(len(k)):
    if str(k[i]) in nn:
        a.append(k[i])
print(a)
