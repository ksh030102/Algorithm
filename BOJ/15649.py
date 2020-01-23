# 15649 N과 M (Silver 3)
def solution(n, m):
    if n == 0:
        return 1
    for i in range(1, m+1):
        if i == n:
            continue
        print(n, i)
    return(n-1, m)


n, m = map(int, input().split())
solution(n, m)
