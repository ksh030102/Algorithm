# 1157
import collections
s = input().upper()
a = collections.Counter(s)
many = []
for k, v in a.items():
    if v == max(a.values()):
        many.append(k)
        if len(many) > 1:
            break
if len(many) == 1:
    print(many[0])
else:
    print('?')

# collections를 배웠다. 진짜 좋은것을 배운것같다. 계속 시간초과가 나왔는데 왜 나온건지 아직도 잘 모르겠지만 풀었다.
    # i = 0
# for key, value in a.items():
#     if value == max(a.values()):
#         if value in list(a.values())[i+1:len(list(a.values()))]:
#             print(-1)
#             break
#         else:
#             print(key)
#             break
#     i += 1