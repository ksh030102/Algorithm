# 1568 새

n = int(input())
i=0
cnt=0
while n!=0: # n을 계속 빼줄때 0이되면 종료
    i+=1
    if n >= i: # i가 n보다 작으면 n에서 i를 뺀다
        n-=i
        cnt +=1 # 카운트 증가
    else: # i가 n보다 크면 게임을 다시 시작하기 때문에 0으로 초기화
        i = 0 # 0으로 초기화하는 이유는 맨위에서 1을 더하면서 시작하기 때문
print(cnt)