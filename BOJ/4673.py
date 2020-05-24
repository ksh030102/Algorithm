# 4673 셀프넘버
# 10이하는 +2 그 이상은 +11인 것 같다.
# 근데 아니었다. 찾아보니까 배열을 만들어서 푸는게 대표적이다.
alist = [int(j) for j in range(1, 10000)]
def self_num(n):
    s = n + sum(int(i) for i in str(n))
    if s > 10000:
        return n - sum(int(i) for i in str(n))
    if s in alist:
        alist[s] == 0
    return self_num(s)
for k in range(len(alist)-1):
    if alist[k] == 0:
        continue
    else:
        self_num(alist[k])
print(*alist)

