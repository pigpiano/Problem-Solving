
n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

# 임시 맵 초기화
temp = [[0] * m for _ in range(n)]
# 바이러스가 상 하 좌 우 이동을 위한 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 바이러스가 퍼진 후 안전 영역의 크기를 구하는 함수 정의
# 이는 벽 3개 설치했다는 가정하에 진행 따라서 임시맵 사용
def get_score():
	cnt = 0
	for i in range(n):
		for j in range(m):
			if temp[i][j] == 0:
				cnt += 1
	return cnt # 안전 영역의 크기 반환
# dfs를 통해 바이러스 퍼지는 함수 정의
# 이는 벽이 3개 다 설치하고 난 후 진행한다는 가정
def virus(x,y):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		# 만약 주어진 범위를 벗어나지 않고, 바이러스가 방문한 적이 없다면
		if (0 <= nx < n) and (0 <= ny < m) and temp[nx][ny] == 0:
			# 해당 위치에 바이러스 퍼지게 한다.
			temp[nx][ny] = 1
			virus(nx,ny) # 재귀적으로 방문
# 이제 벽을 3개 설치하는 모든 경우의 수를 dfs를 통해 구현한다.
ans = 0
def dfs(count): # count는 벽의 수
	global ans
	if count == 3: # 벽 3개 설치했다면
		for i in range(n):
			for j in range(m):
				# 임시맵에 벽 설치한 맵을 임시로 대입
				temp[i][j] = graph[i][j]
		# 각 바이러스 퍼지게 한다.
		for i in range(n):
			for j in range(m):
				if temp[i][j] == 2: # 바이러스가 있는 위치
					virus(i,j) # 바이러스 퍼지게한다.
		# 바이러스 다퍼졌으면 안전 영역의 크기 구해서 비교한다.
		# 최댓값으로 갱신한다.
		ans = max(ans, get_score())
		return
	else: # 벽이 아직 3개가 설치 되지 않았다면
		# 벽을 설치한다.
		for i in range(n):
			for j in range(m):
				if graph[i][j] == 0:
					graph[i][j] = 1 # 벽을 설치
					count += 1
					# 재귀적으로 반복
					dfs(count)
					# 재귀가 끝난 후 다음 벽 설치를 위해 벽 제거
					graph[i][j] = 0
					count -= 1
# 함수 수행
dfs(0) # 처음에는 벽이 0이라고 설정
print(ans)
