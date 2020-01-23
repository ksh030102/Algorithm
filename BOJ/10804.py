# 10804 카드 재배치 (Bronze 2)

def solution():
    card = [i for i in range(1, 21, 1)]
    j = 0
    while j != 10:
        a, b = map(int, input().split())
        card[a-1:b] = list(reversed(card[a-1:b]))
        j += 1
    for i in card:
        print(i, end=' ')

solution()