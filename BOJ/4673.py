# 4673 셀프넘버
# 10이하는 +2 그 이상은 +11인 것 같다.
# 근데 아니었다. 찾아보니까 배열을 만들어서 푸는게 대표적이다.
# 뻘 짓 할 뻔 했 다.

def d(n):
    res = 0
    for i in str(n):
        res += int(i)
    c = res + n
    return c
a = []
for i in range(1, 10001):
    k = d(i)
    a.append(k)
for i in range(1, 10001):
    if i in a:
        pass
    else:
        print(i)