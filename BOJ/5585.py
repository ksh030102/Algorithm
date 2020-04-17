# 5585 거스름돈
pay = 1000-int(input())
cnt = 0
if pay >= 500:
    cnt += pay // 500
    pay %= 500
if pay >= 100:
    cnt += pay // 100
    pay %= 100
if pay >= 50:
    cnt += pay // 50
    pay %= 50
if pay >= 10:
    cnt += pay // 10
    pay %= 10
if pay >= 5:
    cnt += pay // 5
    pay %= 5
if pay >= 1:
    cnt += pay // 1
    pay %= 1
print(cnt)