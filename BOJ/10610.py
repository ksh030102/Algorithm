# 10610 30
def solution():
    num = input()
    a = sorted(num, reverse=True)
    if a[len(num)-1] != '0':
        return -1
    num = ''
    for i in a:
        num += i
    if int(num)%3!=0:
        return -1
    return num
print(solution())