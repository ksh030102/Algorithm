n = int(input())
people = list(map(int, input().split()))
print(n - len(set(people)))