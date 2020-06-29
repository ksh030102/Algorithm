n = int(input())
gul = list(map(int, input().split()))
s = []
for i in range(len(gul)):
    for j in range(i, len(gul)):
        s.append(sum(gul[i:j+1]))
print(max(s))
