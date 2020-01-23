# 5543 상근날드 (Bronze 4)
ham = []
for i in range(5):
    ham.append(int(input()))
print(min(ham[:3])+min(ham[3:])-50)
