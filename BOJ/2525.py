# 2525 오븐 시계

a, b = map(int, input().split())
need = int(input())
n = divmod(need, 60)
a, b = a+n[0], b+n[1]
if b >= 60:
    b -= 60
    a+=1
if a >= 24:
    a-=24
print(a, b)