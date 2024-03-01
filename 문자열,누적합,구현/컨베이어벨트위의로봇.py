
# 회전을 쉽게 하기 위해 deque 사용
from collections import deque

n, k = map(int, input().split())
# 길이가 2인 벨트 deque로 구현
belt = deque(list(map(int, input().split())))
# n길이의 로봇 유무를 저장하는 배열 만들기
robot = deque([0] * n)

result = 0
# 몇 번 반복하는지 정해 지지 않아서 while loop 사용
while True:
	# 1단계씩 증가
	result += 1
	# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
	belt.rotate(1)
	# 로봇과 함께 회전
	robot.rotate(1)
	# 로봇이 내리는 위치에 도달할 경우 즉시 내림
	robot[-1] = 0
	# 2. 이동가능하면 이동, 못하면 가만히
	# 이동 하려면 앞칸에 로봇 없고, 내구도 1이상
	# 내리는 칸이 n-1이므로 n-2부터 시작
	for i in range(n-2, -1, -1):
		if belt[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
			robot[i+1] = 1
			robot[i] = 0
			# 그 칸의 내구도 감소
			belt[i+1] -= 1
	# 내리는 위치에 도달한 경우, 즉시 내림
	robot[-1] = 0
	# 3. 올리는 위치에 내구도 0 아니면 로봇 올려
	if belt[0] != 0 and robot[0] != 1:
		robot[0] = 1 # 로봇 올리기
		belt[0] -= 1
	# 4. 내구도 0인 칸의 수가 k 이상이면 종료
	if belt.count(0) >= k:
		break
print(result)


