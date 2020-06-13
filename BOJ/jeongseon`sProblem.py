# 시간 더하기 3
print('오늘은 6월 30일, 지금시간은 오전 10시입니다.')
print('몇시간 후의 시간을 알려드릴까요?')
thirtyDays = [4, 6, 9, 11]              # 30일 배열
thirtyOneDays = [1, 3, 5, 7, 8, 10, 12] # 31일 배열
anyDays = [2]                           # 나머지 배열
a = int(input())
time = a + 10
month = 6           # 현재 월
day = 30            # 현재 일자
while time > 24:    # 총시간이 24를 넘으면
    time -= 24      # 총시간에서 24를 빼고
    day += 1        # 하루가 지났음으로 하루를 더함
    if (day > 30 and month in thirtyDays) or (day > 31 and month in thirtyOneDays) or (day > 29 and month in anyDays):
        # 30일이 지났고, 총 일이 30일이면   or   31일이 지났고 총 일이 31일이면       or  29일이 지났고 총일이 28일이면 (2020년 기준 윤년이므로 29일)
        # 월과 일이 이미 주어졌지만 그냥 생각해보다 여기까지 오게되었다. 나중에 월과 일도 입력받게 되면 유용하게 사용될 것이다.
        # 5번문제에는 적용하지않았다. 버전이 다름을 알기 위해서
        day = 1
        month += 1
now = ""            # 오전인지 오후인지를 담을 변수
cnt = 0             # 오전오후가 몇번바뀌었는지 카운트하는 변수
while time > 12:    # 총시간이 12를 넘으면
    time -= 12      # 총시간에서 12를 빼고
    cnt += 1        # 바뀌었다는 의미로 1을 더함
if cnt % 2 == 0:    # 현재 오전에서 짝수번 바뀌면 그대로 오전
    now = "오전"
else:               # 현재 오전에서 홀수번 바뀌면 오후
    now = "오후"
print(month, "월", day, "일", now, time,"시")