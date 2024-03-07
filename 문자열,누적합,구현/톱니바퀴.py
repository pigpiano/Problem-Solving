#입력
from collections import deque
t = [deque(list(map(int,input().rstrip()))) for _ in range(4)] # 톱니 상태 저장

# 톱니 돌리기
k = int(input())
for _ in range(k):
	r = [] # 처음 톱니 상태 저장
	for i in range(4):
		r.append([t[i][6],t[i][2]]) # 톱니바퀴가 닿는 위치 저장
	n,d = map(int,input().split())
	n = n-1

	# 왼쪽에 있는 톱니들 돌리기
	if n != 0: # 맨 왼쪽 톱니는 왼쪽을 확인할 필요가 없다.
		for i in range(n,0,-1): # 선택된 톱니부터 왼쪽으로 하나씩 확인
			if r[i][0] != r[i-1][1]: # 현재 톱니의 6번째와 왼쪽의 2번째가 극이 다른지 확인
				if (n-(i-1)) % 2 == 0: # 짝수이면
					t[i-1].rotate(d)
				elif (n-(i-1)) % 2 != 0: # 홀수이면
					t[i-1].rotate(-1*d)
			elif r[i][0] == r[i-1][1]: # 같은 극성을 갖는다면
				break
	if n != 3:
		for i in range(n,3):
			if r[i][1] != r[i+1][0]:
				if (n-(i+1)) % 2 == 0:
					t[i+1].rotate(d)
				elif (n-(i+1)) % 2 != 0:
					t[i+1].rotate(-1*d)
			elif r[i][1] == r[i+1][0]: # 극성이 같다면
				break
	t[n].rotate(d) # 현재 톱니 돌리기

# 출력
# 12시 방향이 N극이면 0점, S극이면 1점
ans = 0
if t[0][0] == 1:
	ans += 1
if t[1][0] == 1:
	ans += 2
if t[2][0] == 1:
	ans += 4
if t[3][0] == 1:
	ans += 8
print(ans)





