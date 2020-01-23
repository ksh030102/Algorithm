# 11721 열 개씩 끊어 출력하기 (Bronze 1)

string = list(input())
for i in range(len(string)):
    if i % 10 == 0 and i != 0:
        print()
    print(string[i], end="")