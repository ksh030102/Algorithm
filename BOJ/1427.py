# 1427 소트인사이드 (Silver 5)

s = int(input())
sl = []
while s != 0:
    sl.append(s%10)
    s//=10
sl.sort(reverse=True)
for i in sl:
    print(i, end='')
