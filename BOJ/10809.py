# 10809
s = input()
a = [-1]*26

for idx, i in enumerate(s):
    if a[ord(i)-97] != -1:
        continue
    a[ord(i)-97] = idx
print(*a)