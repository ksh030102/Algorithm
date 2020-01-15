# 2839 설탕 배달

import sys

def solution():
    sugar = int(sys.stdin.readline())
    package = 0
    while sugar > 0:
        if sugar % 5 != 0:
            sugar -= 3
            if sugar < 0:
                package = -1
                break
            package += 1
        elif sugar % 5 == 0:
            package += 1
            sugar -= 5
        elif sugar % 5 != 0 and sugar % 3 != 0:
            package = -1
    print(package)
solution()
