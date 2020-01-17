# 2447 별찍기 - 10 (Silver 1)

# 9
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********

# 3
# ***
# * *
# ***
def solution():
    a = int(input())
    # for i in range(1,a+1):
    #     print('*'*a)
    for i in range(1, a+1):
        # if i % 3 == 2:
        #     print("* *"*(a//3))
        # elif i>(a/3) and i<((a/3)*2)+1:
        #     print("   "*(a//3))
        # else:
        #     print('***'*(a//3))
        print('*')

 # 중간을 뚫을 수 있는 희망 a < x < a*2 + 1 or a < x <= a*2
 # ex. 3 < 4,5,6 <= 6
solution()