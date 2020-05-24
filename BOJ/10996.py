# 10996 별찍기 21

a = int(input())
for i in range(a*2):
    for j in range(a):
        if i % 2 == 0:
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j % 2 != 0:
                print("*", end="")
            else:
                print(" ", end="")
    print("")
