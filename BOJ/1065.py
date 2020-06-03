# 1065 한수

# 한수는 각자리의 차이 ex. 123 -> 1과 2 2와 3의 차이가 같은 수이다.
n = int(input())

def d(n, cnt=0):
    if n < 100:
        return n
    elif n < 110:
        return 99
    else:
        for i in range(111, n+1):
            if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
                cnt += 1
        return 99+cnt
print(d(n))
