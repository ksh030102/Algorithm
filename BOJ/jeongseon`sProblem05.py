# 시간 더하기 미션 2

print('오늘은 12일, 지금 시간은 10시입니다.')
print('몇시간 후의 시간을 알려드릴까요?')
a = int(input())
time = a + 10 # 총 시간을 구함
day = 12    # 현재 일자
while time > 24:    # 총시간이 24를 넘으면
    time -= 24      # 총시간에서 24를 빼고
    day += 1        # 하루가 지났음으로 하루를 더함
now = ""            # 오전인지 오후인지를 담을 변수
cnt = 0             # 오전오후가 몇번바뀌었는지 카운트하는 변수
while time > 12:    # 총시간이 12를 넘으면
    time -= 12      # 총시간에서 12를 빼고
    cnt += 1        # 바뀌었다는 의미로 1을 더함
if cnt % 2 == 0:    # 현재 오전에서 짝수번 바뀌면 그대로 오전
    now = "오전"
else:               # 현재 오전에서 홀수번 바뀌면 오후
    now = "오후"
print(day, "일", now, time, '시')