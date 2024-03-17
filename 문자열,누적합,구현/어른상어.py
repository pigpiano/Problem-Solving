
n, m, k = map(int, input().split())
# 모든 상어의 위치와 맵 입력받기
data = [list(map(int, input().split())) for _ in range(n)]
# 상어의 초기 방향 정해주기
directions = list(map(int, input().split()))
# 상어의 상황별 우선순위 받아오기 (위 아래 왼쪽 오른쪽)
priorities = [[] for _ in range(m)]
for i in range(m):
	for j in range(4):
		priorities[i].append(list(map(int, input().split())))
# for i in priorities:
# 	print(i)

# 상어 이동을 위한 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 각 상어마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0,0]] * n for _ in range(n)]

# 모든 냄새 정보 업데이트
def update_smell():
	# 각 위치를 확인하며
	for i in range(n):
		for j in range(n):
			# 냄새가 남아 있는 경우, 1만큼 감소시키기
			if smell[i][j][1] > 0:
				smell[i][j][1] -= 1 # 한칸 이동할 때 마다 냄새 줄어든다.
			# 상어가 존재하는 위치의 경우, 해당 위치의 냄새를 k로 설정
			if data[i][j] != 0:
				# 상어 번호, 냄새 머무는 초기시간 삽입
				smell[i][j] = [data[i][j], k]
# 모든 상어 이동시키는 함수
def move():
	# 이동 결과를 담기 위한 임시 테이블 초기화
	new_data = [[0] * n for _ in range(n)]
	# 각 위치를 하나씩 확인하며
	for x in range(n):
		for y in range(n):
			# 상어가 존재하면
			if data[x][y] != 0: # 상어의 위치라는 뜻
				# 방향 1 ~ 4 이지만 컴터는 0 ~ 3
				# 현재 상어의 방향
				direction = directions[data[x][y] - 1] # index 재조정
				flag = False # 초기화
				# 일단 냄새가 존재하지 않은 곳이 있는지 확인
				for index in range(4):
					nx = x + dx[priorities[data[x][y]-1][direction-1][index]-1]
					ny = y + dy[priorities[data[x][y]-1][direction-1][index]-1]
					if (0<=nx<n) and (0<=ny<n):
						# 냄새가 나지 않는 곳이라면 1순위
						if smell[nx][ny][1] == 0:
							# 해당 상어의 방향 이동시키기
							directions[data[x][y]-1] = priorities[data[x][y]-1][direction-1][index]
							# 상어 이동 시키기
							if new_data[nx][ny] == 0:
								new_data[nx][ny] = data[x][y]
							else: # 만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록
								new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
							flag = True
							break
				if flag:
					continue
				# 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
				for index in priorities[data[x][y] - 1][direction - 1]:
					nx = x + dx[index -1]
					ny = y + dy[index -1]
					if (0<=nx<n) and (0<=ny<n):
						# 자신의 냄새가 있는 곳이라면
						if smell[nx][ny][0] == data[x][y]:
							# 해당 상어 방향 변경
							directions[data[x][y]-1] = index
							# 상어 이동시키기
							new_data[nx][ny] = data[x][y]
							break
	return new_data

time = 0 # 0초 부터 시작
while True:
	update_smell() # 모든 위치의 냄새 업데이트
	new_data = move() # 모든 상어를 이동시키기
	data = new_data # 맵 업데이트
	time += 1 # 시간 증가

	# 1번 상어만 남았는지 확인
	check = True
	for i in range(n):
		for j in range(n):
			# 번호 1보다 큰게 있다면
			if data[i][j] > 1:
				check = False
	if check:
		print(time)
		break
	# 1000초가 지날 때까지 끝나지 않았다면
	if time >= 1000:
		print(-1)
		break






