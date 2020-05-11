n, m = map(int,input().split())
xylist = []
ablist = []

for i in range(n):
    xylist.append(list(map(int, input().split())))
for j in range(m):
    ablist.append(list(map(int, input().split())))
ab = [[ablist[0][0], ablist[0][1]]]
cnt = 0
k = 0
sorted(ablist)
while k < len(ablist):
    print(ablist[k][cnt])
    if ablist[k][0] in ab[cnt] or ablist[k][1] in ab[cnt]:
        ab.insert(cnt, ablist[k][0])
        ab.insert(cnt, ablist[k][1])
    else:
        ab.append([ablist[k][0], ablist[k][1]])
        cnt += 1
    k+=1
print(ab)