#14681 사분면 고르기 단계별로 풀어보기 시작

a = int(input())
b = int(input())

if a > 0 and b > 0:
    print(1)
elif a > 0 and b < 0:
    print(4)
elif a < 0 and b < 0:
    print(3)
else:
    print(2)