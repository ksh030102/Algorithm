# 2908 상수

a, b = map(str, input().split())
a = list(reversed(a))
b = list(reversed(b))
for i in range(3):
    if a[i] > b[i]:
        print(*a, end="")
        break
    elif a[i] < b[i]:
        print(*b)
        break