# 1094 막대기 (Silver 5)

want = int(input())
bl = [64]
while sum(bl) != want:
    if sum(bl) > want:
        bl[len(bl)-1] //= 2
    else:
        bl.append(bl[len(bl)-1]//2)
        if sum(bl) < want:
            bl.append(bl[len(bl) - 2] // 2)
print(len(bl))