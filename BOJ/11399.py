# 11399 ATM
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1: # n이 1일 때 아무도 기다릴 필요가 없으므로 return
        return a[0]
    a.sort() # 시간이 짧은 순서대로 정렬
    j = s = a[0]
    for i in range(len(a)-1):
        j = j + a[i+1] # 이번 사람이 기다린 시간을 누적
        s += j # 총 기다린 시간을 누적
    return s
print(solution())
