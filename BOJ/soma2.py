n = int(input())
alist = []
for i in range(n):
    s, e = map(int, input().split())
    alist.append([s, e])
for j in range(n):
    cnt = 0
    for k in range(n):
        if alist[j][0] > alist[k][0] and alist[j][0] < alist[k][1]:
            cnt += 1
    print(cnt)
