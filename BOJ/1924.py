# 2007년 (Bronze 1)
d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, date = map(int, input().split())
'''
m 리스트에 month 번째까지 더한다음 7로 나누고 date를 더해보자
'''
s = sum(m[:month])+date
print(d[s%7])
# 1월 1일 MON
# 2월 1일 THU
# 3월 1일 THU
