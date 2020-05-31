# 2869

a, b, v = map(int, input().split())
now, cnt = 0, 1
while now < v:
    now += a
    if now >= v:
        break
    now -= b
    cnt += 1
print(cnt)