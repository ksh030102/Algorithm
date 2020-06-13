# 두수를 입력받아 모든 사칙연산 결과를 보여주는 계산기

a, b = map(int,input().split())
print("a + b = ", (a+b))    # 더하기
print("a - b = ", (a-b))    # 빼기
print("a * b = ", (a*b))    # 곱하기
print("a // b = ", (a//b))  # 몫 구하기
print("a % b = ", (a % b))  # 나머지 구하기