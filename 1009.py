import sys
t = int(sys.stdin.readline())
for i in range(t):


    a, b = map(int, sys.stdin.readline().split())
    temp = 1
    result_list = []
    for _ in range(b):
        temp *= a
        temp %= 10
        if temp in result_list:
            break
        result_list.append(temp)
    result = result_list[b%len(result_list) - 1]
    if result == 0:
        print(10)
    else:
        print(result)
