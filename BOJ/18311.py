# 18311 왕복

# def solution():
#     n, dis = map(int, input().split())
#     cnt = 1
#     b = list(map(int, input().split()))
#     b += b[::-1]
#     i = 0
#     for i in range(len(b)//2):
#         if dis >= 0:
#             dis-=b[i]
#             cnt+=1
#         else:
#             break
#     if cnt > n:
#         cnt = n
#     for i in range(len(b)):
#         if dis>=0:
#             dis-=b[i]
#             cnt-=1
#         else:
#             break
#     print(cnt)
# solution()
n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr += arr[::-1]

for i in range(len(arr)):
    k -= arr[i]
    if k < 0:
        if i > n-1:
            print(n*2-i)
            exit()
        else:
            print(i+1)
            exit()
    elif k == 0:
        if i > n-1:
            print(n*2-i-1)
        else:
            print(i+2)
            exit()