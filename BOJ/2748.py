# 2748
a, b = 0, 1
c = [a, b]
def f(n):
    if n == 1:
        return
    c.insert(len(c), c[len(c)-2] + c[len(c)-1])
    f(n-1)
n = int(input())
f(n)
print(c[n])