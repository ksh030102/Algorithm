# n = int(input())
# 0 1 2 3 4 5 6 7 8 9
# 00 01 02 03 04 05 06 07 08 09 11 12 13 14 - - 22 23 24 25 26 27 28 29 <-> 99
#2 -> 10 + 9 + 8 + 7 + ... + 1
# 000 001 002 003 004 005 006 007 008 009
# 011 012 013 014 015 016 017 018 019
# 022 023 024 025 026 027 028 029
# 033 034 035 036 037 038 039
# ----
# 099

# 111 112 113 114 115 116 117 118 119
# 122 123 124 125 126 127 128 129
# 133 134 135 136 137 138 139
# 144 145 146 147 148 149
# 155 156 157 158 159
# 166 167 168 169
# 177 178 179
# 188 189
# 199
[10, 55, 220, 715]
# 0999
# 220개
# 45
# 36
# 1111 1112 1113 1114 1115 1116 1117 1118 1119 -> 9
# 1122 1123 1124 1125 1126 1127 1128 1129 -> 8
# 1133 1134->7
# 1144->6
# 1155->5
# 1166->4
# 1177 ->3
# 1188->2
# 1199->1
# 1222 1223 1224 1225 1226 1227 1228 1229
# 1 -> 165
# 2 -> 120
# 3 -> 84
# 4 -> 56
# 5 -> 35
# 6 -> 20
# 7 -> 10
# 8 -> 4
# 9 -> 1
# 2222 2223 2224 2225 2226 2227 2228 2229
# 9999
# sum = 0
# while i > 0:
#     for j in range(1, i + 1):
#         sum += j
#     i -= 1
# print(sum)
# print(165+120+84+56+35+20+10+4+1+220)
# def dp(n):
#     sum = 0
#     for l in range(n):
#         for k in range(10):
#             i = 10 - k
#             while i > 0:
#                 for j in range(1, i+1):
#                     sum += j
#                 i -= 1
#     print(sum)
# dp(int(input()))
num = [i for i in range(1, 11)]

def dp(n):
    if n == 1:
        return 10
    for j in range(n-2):
        for i in range(1, 10):
            num[i] += num[i-1]
    return sum(num) % 10007
print(dp(int(input())))